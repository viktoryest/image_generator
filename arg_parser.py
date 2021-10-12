import argparse


def create_parser():
    parser = argparse.ArgumentParser(prog='Image Generator', description='An easy way to create '
                                                                         'images from your spreadsheet')
    parser.add_argument('-n', '--name', default='test_table.xlsx', help='path to the spreadsheet')
    parser.add_argument('-sh', '--sheet', default='0', help='number or title of the sheet')
    parser.add_argument('-f', '--font', default='times.ttf', help='necessary font')
    parser.add_argument('-b', '--back', default='#ffffff', help='background colour')
    parser.add_argument('-t', '--text', default='#000000', help='text colour')
    parser.add_argument('-s', '--size', default=80, help='text size')
    parser.add_argument('-w', '--wpad', default=20, help='width padding')
    parser.add_argument('-hp', '--hpad', default=10, help='height padding')
    parser.add_argument('-p', '--path', default='images', help='path to the folder')
    return parser
