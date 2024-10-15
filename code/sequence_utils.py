from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Align.Applications import ClustalOmegaCommandline
from IPython.display import HTML, display
import tempfile
import os
import re

def highlight_sequence(sequence, highlight_positions=None, highlight_substrings=None, sequence_label=None, intensity_mappings=None):
    """
    Display a protein sequence in Jupyter and highlight specific positions or substrings with background colors.
    Additional intensity mappings are displayed as blue-shaded lines.
    
    sequence: str, the protein sequence
    highlight_positions: dict, where keys are the positions (1-based) and values are the background color to highlight in
    highlight_substrings: dict, where keys are substrings and values are the background color to highlight in
    sequence_label: str, a label to display before the sequence on the same line
    intensity_mappings: list of dict, where each dict contains mappings of positions to intensity (0-100)
    """
    colored_sequence = list(sequence)
    
    # Highlight substrings first
    if highlight_substrings:
        for substring, bg_color in highlight_substrings.items():
            for match in re.finditer(re.escape(substring), sequence):
                start = match.start()
                end = match.end()
                for i in range(start, end):
                    colored_sequence[i] = f'<span style="background-color:{bg_color}">{colored_sequence[i]}</span>'
    
    # Highlight specific positions and overwrite any existing color if needed
    if highlight_positions:
        for pos, bg_color in highlight_positions.items():
            pos = pos - 1  # Adjust for 1-based indexing
            if pos < len(colored_sequence):
                colored_sequence[pos] = f'<span style="background-color:{bg_color}">{sequence[pos]}</span>'
    
    # Join the colored sequence back together
    colored_sequence = ''.join(colored_sequence)
    
    # Create 1-based position markers every 10 characters
    position_line = ''.join([f'{i:<10}' for i in range(1, len(sequence)+1, 10)])
    
    # Display label and sequence in the same line if provided
    label_display = f"<h3>{sequence_label}</h3>" if sequence_label else ""
    
    # Prepare the base sequence lines with blue intensity mapping
    intensity_lines = ""
    if intensity_mappings:
        for mapping in intensity_mappings:
            intensity_line = []
            for i in range(len(sequence)):
                intensity = mapping.get(i+1, 0)  # 1-based indexing, default to 0
                blue_intensity = 255- int(255 * (intensity / 100))  # Scale to 0-255 for rgba
                intensity_line.append(f'<span style="background-color:rgba({255-blue_intensity}, 125, {255-blue_intensity}, 0.35);">{sequence[i]}</span>')
            intensity_lines += ''.join(intensity_line) + "\n"
    
    # Display position markers, label, sequence, and intensity-mapped lines
    display(HTML(f'<pre style="font-size:16px; font-family:monospace;">{label_display}\n{position_line}\n{colored_sequence}\n{intensity_lines}</pre>'))


def align_sequences_biopython(sequences, sequence_names):
    """
    Perform multiple sequence alignment (MSA) on a list of sequences using Biopython's built-in aligner.
    
    Parameters:
    - sequences: List of sequences to align.
    - sequence_names: List of names for each sequence.
    
    Returns:
    - A MultipleSeqAlignment object with the aligned sequences.
    """
    # Create temporary files for input and output
    input_file = tempfile.NamedTemporaryFile(delete=False, suffix=".fasta")
    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".aln")

    # Write the sequences to the input FASTA file
    with open(input_file.name, "w") as f:
        for name, seq in zip(sequence_names, sequences):
            f.write(f">{name}\n{seq}\n")
    
    # Perform alignment using Clustal Omega
    clustalomega_cline = ClustalOmegaCommandline(infile=input_file.name, outfile=output_file.name, verbose=True, auto=True, force=True)
    clustalomega_cline()

    # Read the alignment
    alignment = AlignIO.read(output_file.name, "fasta")

    # Clean up temporary files
    os.remove(input_file.name)
    os.remove(output_file.name)

    return alignment

def highlight_differences_in_alignment(alignment):
    """
    Highlight differences in a multiple sequence alignment and return formatted HTML for display in Jupyter.
    
    Parameters:
    - alignment: A MultipleSeqAlignment object.
    
    Returns:
    - A string of HTML content to display the alignment with highlighted differences.
    """
    num_sequences = len(alignment)
    alignment_length = alignment.get_alignment_length()
    
    # Get the sequence IDs and find the max length for padding
    sequence_ids = [record.id for record in alignment]
    max_id_length = max(len(seq_id) for seq_id in sequence_ids)
    
    # Create a color-coded alignment display
    html_content = "<pre style='font-size:14px; font-family:monospace;'>"
    
    # Loop through each sequence and display aligned residues
    for i in range(num_sequences):
        # Pad the sequence ID to align the names properly
        seq_id = sequence_ids[i].ljust(max_id_length)
        html_content += f"{seq_id} "
        
        for j in range(alignment_length):
            column_residues = [alignment[k, j] for k in range(num_sequences)]
            if len(set(column_residues)) == 1:
                # If all residues in the column are the same, display in black
                html_content += f"<span>{alignment[i, j]}</span>"
            else:
                # Highlight differences in red
                html_content += f"<span style='background-color: yellow;'>{alignment[i, j]}</span>"
        
        html_content += "\n"
    
    html_content += "</pre>"
    
    return html_content

def display_alignment_with_highlighting(alignment):
    """
    Display a multiple sequence alignment with highlighted differences in Jupyter.
    
    Parameters:
    - alignment: A MultipleSeqAlignment object to display.
    """
    html_content = highlight_differences_in_alignment(alignment)
    display(HTML(html_content))

