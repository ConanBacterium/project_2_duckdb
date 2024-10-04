import os
import statistics
import re
from collections import defaultdict

def process_files(filepaths, line_numbers, output_filepath):
    numbers_by_line_and_position = defaultdict(lambda: defaultdict(list))
    
    # Extract numbers from specified lines
    for filepath in filepaths:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                return "WRONG FILEPATH"
            for line_num in line_numbers:
                if 0 <= line_num < len(lines):
                    # Extract all numbers from the line
                    matches = re.findall(r'\d+(?:\.\d+)?', lines[line_num])
                    if matches:
                        for pos, match in enumerate(matches):
                            numbers_by_line_and_position[line_num][pos].append(float(match))
                    else:
                        return f"NO NUMBER ON GIVEN LINENUMBER ({line_num}) IN {filepath} \n {lines[line_num]}"
    
    # Calculate mean, standard deviation, and CV for each line and number position
    stats_by_line = {}
    for line_num, positions in numbers_by_line_and_position.items():
        stats_by_line[line_num] = []
        for pos, numbers in positions.items():
            if numbers:
                mean = statistics.mean(numbers)
                std_dev = statistics.stdev(numbers) if len(numbers) > 1 else 0
                cv = 0 if mean == 0 else std_dev / abs(mean)
                stats_by_line[line_num].append((mean, std_dev, cv))
    
    # Create the output file
    with open(filepaths[0], 'r') as input_file, open(output_filepath, 'w') as output_file:
        for i, line in enumerate(input_file):
            if i in stats_by_line:
                new_line = line
                numbers = re.findall(r'\d+(?:\.\d+)?', new_line)
                for j, (mean, std_dev, cv) in enumerate(reversed(stats_by_line[i])):
                    if j < len(numbers):
                        replacement = f"(mean: {mean:.5f}, std: {std_dev:.5f}, cv: {cv:.5f})"
                        new_line = new_line.replace(numbers[-(j+1)], replacement, 1)
                output_file.write(new_line)
            else:
                output_file.write(line)
    
    return f"Process completed. Output file saved as {output_filepath}"

######## q1
# threadcount 1
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_1/q1/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9, 58, 64, 72, 81, 95, 115]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount1_q1.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)
# threadcount 4
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_4/q1/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9, 58, 64, 72, 81, 95, 115]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount4_q1.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)
# threadcount 8
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_8/q1/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9, 58, 64, 72, 81, 95, 115]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount8_q1.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)


######## q2
# threadcount 1
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_1/q2/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9, 76, 85, 97, 107, 119, 131, 141, 161, 175, 189, 204, 218, 234]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount1_q2.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)
# threadcount 4
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_4/q2/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9, 76, 85, 97, 107, 119, 131, 141, 161, 175, 189, 204, 218, 234]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount4_q2.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)
# threadcount 8
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_8/q2/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9, 76, 85, 97, 107, 119, 131, 141, 161, 175, 189, 204, 218, 234]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount8_q2.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)


######## q3
# threadcount 1
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_1/q3/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9,76,85,97,107,119,131,141,161,175,189,203,220]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount1_q3.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)
# threadcount 4
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_4/q3/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9,76,85,97,107,119,131,141,161,175,189,203,220]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount4_q3.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)
# threadcount 8
filepaths = [f"ssb_10/outputs/hot_repetition/threadcount_8/q3/profile_{i}.md" for i in range(50)]
del filepaths[0] # rm first profiling because it is cold
line_numbers_ = [9,76,85,97,107,119,131,141,161,175,189,203,220]
line_numbers = [line_numbers_[i]-1 for i in range(len(line_numbers_))]
output_filepath = 'ssb_10/aggregated_profiling/ssb_10_threadcount8_q3.md'
result = process_files(filepaths, line_numbers, output_filepath)
print(result)