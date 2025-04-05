from data import data
import pprint

def format_applications_for_internal_role(data):
    parent_map = {}

    for parent, child in data:
        parent_map[parent] = parent_map.get(parent, [])     
        parent_map[parent].append(child)

    all_children = set(child for _, child in data) # So I know strategic planning is a child
    root_nodes = [parent for parent in parent_map if parent not in all_children] # So if anything is a child, it won't be in the root nodes

    hierarchy = []  
    for root in root_nodes:
        tree = _build_tree(root, parent_map, set())
        if tree:    
            hierarchy.append(tree)  
    
    return hierarchy

def _build_tree(node_name, parent_map, processed_nodes):
        # This should not happen, as that means the data is cyclical: A-B-C-A
        # We check in order to avoid infinite recursion in case of bad data
        if node_name in processed_nodes:
            return None  

        processed_nodes.add(node_name)
        node = {"name": node_name}

        if node_name in parent_map:
            children = []
            for child in parent_map[node_name]:
                child_node = _build_tree(child, parent_map, processed_nodes)
                if child_node:  # Only add if not None (not already processed)
                    children.append(child_node)
            if children:  # Only add children if there are any
                node["children"] = children

        # When a node is not in parent_map, it means it has no children, we return
        # example: "tracking" is not a parent of anything
        # If a node is in parent_map, it means it has children, the recursive will continue
        return node



result = format_applications_for_internal_role(data)
pprint.pprint(result)


