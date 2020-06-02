import csv
import argparse
import os


def create_data(filename):
    d = {}
    with open(filename) as f:
        read_csv = csv.reader(f)
        header = next(read_csv)
        for i in range(len(header)):
            if header[i] == 'Total Hospital Beds':
                thb = i
            if header[i] == 'Available Hospital Beds':
                ahb = i
        for row in read_csv:
            try:
                total = float(row[thb].replace(',', ''))
                available = float(row[ahb].replace(',', ''))
                d[row[0]] = available/total
            except ValueError:
                continue
        return d


def sort_dict(d, number):
    res = []
    sorted_d = sorted(d.items(), key=lambda k: k[1], reverse=True)
    try:
        for row in range(number):
            res.append(sorted_d[row])
    except IndexError:
        print(f'''This data is too small for you.
I have only {len(d)} elements(''')
    return res


def formatting_result(res_list):
    res = ''
    for i in res_list:
        res += ' {} {}%\n'.format(i[0], round(i[1]*100, 1))
    return res


def main():
    parser = argparse.ArgumentParser(
        description='''
        This program can calculate percent of available
        beds and output HRR with N highest percent.
        Information you can take from csv-file
        HRR Scorecard_ 20 _ 40 _ 60 - 20 Population.csv.
        You need to write a path to this file.
        Number of beds you can choose yourself
        in second argument'''
    )
    parser.add_argument('-path',
                        type=str, help='Path to CSV file')
    parser.add_argument('-bed',
                        type=int, help='Number of beds')
    args = parser.parse_args()
    file_path = os.path.join(args.path,
                'HRR Scorecard_ 20 _ 40 _ 60 - 20 Population.csv')
    try:
        return formatting_result(sort_dict(create_data(file_path),
                                      args.bed))
    except FileNotFoundError:
        return 'There is no file in this directory'


if __name__ == '__main__':
    print(main())
