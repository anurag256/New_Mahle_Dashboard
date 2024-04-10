from xml.etree import ElementTree as ET
import logging
from colorlog import ColoredFormatter
from lxml import etree

# CREATING LOGGER
log = logging.getLogger('example_logger')
log.setLevel(logging.DEBUG)
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-s:%(lineno)-s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)


def svg_gen(colors: list, name: str) -> str:
    match name:
        # Case for S generation
        case "s":
            tree = ET.parse("resources/SVG/S.svg")
            root = tree.getroot()
            for index, color in enumerate(colors):
                index += 1
                if index < 10:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}']")
                else:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}_']")
                target_element.set("fill", color)
            try:
                tree.write("resources/SVG-out/s.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        #     Case for D Generation
        case "d":
            tree = ET.parse("resources/SVG/D.svg")
            root = tree.getroot()
            for index, color in enumerate(colors):
                index += 1
                if index < 10:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}']")
                else:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}_']")
                target_element.set("fill", color)
            try:
                tree.write("resources/SVG-out/d.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        case "q":
            tree = ET.parse("resources/SVG/Q.svg")
            root = tree.getroot()
            for index, color in enumerate(colors):
                index += 1
                if index < 10:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}']")
                else:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}_']")
                target_element.set("fill", color)
            try:
                tree.write("resources/SVG-out/q.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        case "c":
            tree = ET.parse("resources/SVG/C.svg")
            root = tree.getroot()
            for index, color in enumerate(colors):
                index += 1
                if index < 10:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}']")
                else:
                    target_element = root.find(f".//*[@id='untitled-u-day{index}_']")
                target_element.set("fill", color)
            try:
                tree.write("resources/SVG-out/c.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        case _:
            return "Please Provide Name of Alphabet"


def clear_svg(tree, root, colors: list, name: str):
    # Define the namespace mapping
    # namespace_mapping = {"": "http://www.w3.org/2000/svg"}
    namespace_mapping = {"": "ns0:"}

    for index, color in enumerate(colors):
        index += 1
        if index < 10:
            target_element = root.find(f".//*[@id='untitled-u-day{index}']")
        else:
            target_element = root.find(f".//*[@id='untitled-u-day{index}_']")
        target_element.set("fill", color)

    # Remove the namespace prefix from all elements
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]  # Remove the namespace prefix
    # Update the namespace in the XML declaration
    if "xmlns" in root.attrib:
        root.attrib["xmlns"] = namespace_mapping[""]
    # Iterate through the elements and update the namespace
    for elem in root.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]
            elem.attrib = {k.split("}", 1)[1]: v for k, v in elem.attrib.items()}
    
    return tree


def new_svg_gen(colors: list, name: str) -> str:
    match name:
        # Case for S generation
        case "s":
            tree = ET.parse("resources/SVG/S.svg")
            root = tree.getroot()
            tree = clear_svg(tree, root, colors, name)
            try:
                tree.write("resources/SVG-out/s.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        #     Case for D Generation
        case "d":
            tree = ET.parse("resources/SVG/D.svg")
            root = tree.getroot()
            tree = clear_svg(tree, root, colors, name)
            try:
                tree.write("resources/SVG-out/d.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        case "q":
            tree = ET.parse("resources/SVG/Q.svg")
            root = tree.getroot()
            tree = clear_svg(tree, root, colors, name)
            try:
                tree.write("resources/SVG-out/q.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        case "c":
            tree = ET.parse("resources/SVG/C.svg")
            root = tree.getroot()
            tree = clear_svg(tree, root, colors, name)
            try:
                tree.write("resources/SVG-out/c.svg")
                return "success"
            except Exception as e:
                log.critical(e)
                return "Generation Failed"

        case _:
            return "Please Provide Name of Alphabet"




if __name__ == "__main__":
    log.debug(svg_gen(["blue", "blue", "purple"], "c"))
