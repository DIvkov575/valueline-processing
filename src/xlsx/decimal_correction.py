"""
Detect Missing Decimal Points
both functions accomplish the same thing, however first allows for more flexibility by calling process() on individual files
both functions are just implementations of the process & process_all from decimal_processing_xlsx_vesmar

decimal_processing_xlsx_vesmar.process(input_path, output_path)
decimal_processing_xlsx_vesmar.process_all(input_dir, output_dir)

"""
import os
from os.path import join
import time
from decimal_processing_xlsx_vesmar import process, process_all


def correct_decimals(input_dir ="input", output_dir ="output"):
    """
    will process all pdfs
    input_dir and output_dir cannot end in slash
    """
    all_files = os.listdir(input_dir)

    start_time = time.time()

    for (index, file) in enumerate(all_files):
        if file.endswith("xlsx"):
            process(join(input_dir, file), join(output_dir, file))
            print(f"{file} ({index + 1}/{len(all_files)})")

    print("execution time: ", time.time() - start_time)


# def correct_decimals_all(input_dir = "input/", output_dir ="output/"):
#     """
#     will process all pdfs
#     note! input and output dir are not created automatically
#     input and output dir names must end in slash
#     """
#
#     start_time = time.time()
#
#     print(os.getcwd() )
#     process_all("input/", "output/")
#
#     print("execution time: ", time.time() - start_time)
