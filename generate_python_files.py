# coding: utf-8

import versioneer
import os

from typing import Dict
from importlib import import_module

from base_node_rpc.helpers import generate_protobuf_python_code, generate_python_code

DEFAULT_ARDUINO_BOARDS = []

PLATFORMIO_ENVS = ['teensy31']


def get_properties(**kwargs) -> Dict:
    version = versioneer.get_version()

    try:
        base_node_version = import_module('base_node_rpc').__version__
    except ImportError:
        base_node_version = None

    module_name = 'mr_box_peripheral_board'
    package_name = module_name.replace('_', '-')
    url = f'https://github.com/sci-bots/{package_name}'

    properties = dict(package_name=package_name,
                      display_name='MR-Box peripherals',
                      manufacturer='Sci-bots Inc.',
                      software_version=version,
                      base_node_software_version=base_node_version,
                      url=url
                      )

    meta = dict(
        short_description='Firmware for MR-Box controller board for various peripherals (e.g., motorized magnet, LED panels, micro pump, temperature/humidity sensor)',
        long_description='',
        module_name=module_name,
        author='Christian Fobel',
        author_email='christian@fobel.net',
        camelcase_name='MrBoxPeripheralBoard',
        version=version,
        license='BSD-3',
        category='Communication',
        architectures='avr',
    )

    lib_properties = {**properties, **meta}

    options = dict(  #pointer_width=32,
        rpc_module=import_module(module_name) if module_name else None,
        module_name=module_name,
        PROPERTIES=properties,
        LIB_PROPERTIES=lib_properties,
        # Classes inherited from headers in `BaseNodeRpc` Arduino library.
        base_classes=['BaseNodeSerialHandler',
                      'BaseNodeEeprom',
                      'BaseNodeConfig<ConfigMessage, Address>'],
        # Classes inherited from headers within sketch directory.
        rpc_classes=['mr_box_peripheral_board::PMT',
                     'mr_box_peripheral_board::Pump',
                     'base_node_rpc::ZStage',
                     'mr_box_peripheral_board::Max11210Adc',
                     'mr_box_peripheral_board::Node'],
        # DEFAULT_ARDUINO_BOARDS=DEFAULT_ARDUINO_BOARDS,
        # PLATFORMIO_ENVS=PLATFORMIO_ENVS,
    )

    return {**kwargs, **options}


def generate_all_python_code(lib_options: Dict) -> None:
    """
    Generate all Python (host) code, but do not compile device sketch or C++ Device code.
    """
    top = f"{'#' * 80} Generating All Python (host) Code {'#' * 80}"
    print(top)

    generate_protobuf_python_code(lib_options)
    generate_python_code(lib_options)

    print(f"{'#' * len(top)}")


def main():
    properties = get_properties(
        prefix=os.getenv("CONDA_PREFIX"),
        source_dir=os.path.dirname(__file__)
    )

    top = '>' * 180
    print(top)

    generate_all_python_code(properties)

    print('<' * len(top))


if __name__ == '__main__':
    main()
