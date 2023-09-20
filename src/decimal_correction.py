"""
Detect Missing Decimal Points

both functions accomplish the same thing, however first allows for more flexibility by calling process() on individual files
"""
import os
from os.path import join
import time
from decimal_processing_xlsx_vesmar import process, process_all


def correct_decimals():
    """
    will process all pdfs
    input and output dir cannot end in slash
    """
    input_path = "input"  # do not add a slash at the end of dir name
    output_path = "output"  # do not add a slash at the end of dir name
    all_files = os.listdir(input_path)

    start_time = time.time()

    for (index, file) in enumerate(all_files):
        if file.endswith("xlsx"):
            process(join(input_path, file), join(output_path, file))
            print(f"{file} ({index + 1}/{len(all_files)})")

    print("execution time: ", time.time() - start_time)


def correct_decimals_all():
    """
    will process all pdfs
    note! input and output dir are not created automatically
    input and output dir names must end in slash
    """

    input_path = "input/"  # adding slash is necessary when using 'process_all'
    output_path = "output/"  # adding slash is necessary when using 'process_all'

    start_time = time.time()
    process_all(input_path, output_path)
    print("execution time: ", time.time() - start_time)
