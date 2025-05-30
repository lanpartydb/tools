"""
lanpartydb_converter.inputs.dotlan.main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DOTLAN Intranet entry point

:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from argparse import ArgumentParser
from pathlib import Path

from lanpartydb_converter.exporter import export_parties

from .loader import load_parties


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('sql_filename', type=Path)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--output-path', type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    parties = load_parties(args.sql_filename, args.base_url)
    export_parties(parties, args.output_path)
