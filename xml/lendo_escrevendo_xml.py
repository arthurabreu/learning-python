import xml
import xml.dom.minidom as minidom
from pathlib import Path

def print_separator():
    """Print a consistent separator line (was previously repeated manually)."""
    print("------------------------")

def save_dom(dom: minidom.Document, out_path: Path, pretty: bool = True) -> None:
    """Persist the DOM to disk.

    Args:
        dom: Parsed minidom Document.
        out_path: Destination file path.
        pretty: If True, write a pretty-formatted version; else raw toxml().
    """
    if pretty:
        # toprettyxml adds extra whitespace; strip blank lines for readability
        raw = dom.toprettyxml(indent="  ")
        cleaned = "\n".join(line for line in raw.splitlines() if line.strip())
        data = cleaned
    else:
        data = dom.toxml()
    out_path.write_text(data, encoding="utf-8")

def add_new_element_to_xml_products(dom: minidom.Document, product_data: dict) -> None:
    """Add a new product element to the XML document.

    Args:
        dom: The XML document.
        product_data: A dictionary containing product information (id, name, price).
    """
    # Create a new product element
    new_product = dom.createElement("product")
    new_product.setAttribute("id", product_data["id"])

    # Create child elements for name and price
    name_element = dom.createElement("name")
    name_element.appendChild(dom.createTextNode(product_data["name"]))
    new_product.appendChild(name_element)

    price_element = dom.createElement("price")
    price_element.appendChild(dom.createTextNode(product_data["price"]))
    new_product.appendChild(price_element)

    # Append the new product to the root element
    dom.documentElement.appendChild(new_product)

def main():
    # construct a path to the products_catalog.xml file inside this script's directory
    xml_path = Path(__file__).parent / 'products_catalog.xml'

    # lendo arquivo xml (debug info)
    print_separator()
    print(f"XML path: {xml_path}")
    print("Exists:", xml_path.exists())
    print("Size:", xml_path.stat().st_size if xml_path.exists() else "N/A")
    print("First 60 bytes:", xml_path.read_text(encoding="utf-8")[:60])
    print_separator()

    domtree = xml.dom.minidom.parse(str(xml_path))  # Carrega o arquivo XML
    print(domtree)
    print_separator()

    group = domtree.documentElement
    tag = group.getElementsByTagName("product")

    print_separator()
    print("Group element:", group, '\n')
    print("tag element:", tag, '\n')

    print("Root element:", group.tagName, '\n')
    print_separator()

    print("Attributes:", group.attributes.items(), '\n')
    print_separator()

    print("Child nodes:", group.childNodes, '\n')
    print_separator()

    print("Child nodes count:", len(group.childNodes), '\n')
    print_separator()

    print("Child nodes names:", [child.nodeName for child in group.childNodes], '\n')
    print_separator()

    print("Child nodes types:", [child.nodeType for child in group.childNodes], '\n')
    print_separator()

    print("Child nodes values:", [child.nodeValue for child in group.childNodes], '\n')
    print_separator()

    print("Child nodes length:", group.childNodes.length)
    print_separator()

    print("Child nodes item(0):", group.childNodes.item(0))
    print_separator()

    print("Child nodes item(1):", group.childNodes.item(1))
    print_separator()

    print("Child nodes item(2):", group.childNodes.item(2))
    print_separator()

    # Iterando por elementos e retornando valores
    for product in tag:
        print("Product element:", product, '\n')
        print("Product ID:", product.getAttribute("id"), '\n')
        print("Product Name:", product.getElementsByTagName("name")[0].firstChild.nodeValue, '\n')
        print("Product Price:", product.getElementsByTagName("price")[0].firstChild.nodeValue, '\n')
        print_separator()

    # Criar um clone do DOM original para gerar o novo arquivo com o produto adicional
    new_dom = domtree.cloneNode(deep=True)

    # Adicionar novo produto apenas ao clone (o domtree original permanece igual)
    add_new_element_to_xml_products(new_dom, {
        "id": "P007",
        "name": "New Product",
        "price": "19.99"
    })

    # Salvar o clone modificado em um novo arquivo XML
    new_xml_path = Path(__file__).parent / 'new_products_catalog.xml'
    save_dom(new_dom, new_xml_path, pretty=True)
    print("Novo arquivo XML (com produto extra) salvo em:", new_xml_path)
    print("Tamanho do novo arquivo:", new_xml_path.stat().st_size, 'bytes')
    print_separator()



if __name__ == "__main__":
    main()