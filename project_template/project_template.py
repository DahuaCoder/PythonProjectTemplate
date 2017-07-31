#!/usr/bin/env python


import argparse


class ProjectTemplate(object):
    """python project template"""

    def __init__(self, path):
        self.start_msg = "start ..."
        self.path = path

    def start(self):
        print(self.start_msg)
        print("The specified path is:")
        print(self.path)


def setup_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        help="specify path for input file")
    return parser


def main():
    # Parse arguments
    parser = setup_argparser()
    args = parser.parse_args()

    dummy = ProjectTemplate(args.path)
    dummy.start()


if __name__ == '__main__':
    main()  # pragma: no cover
