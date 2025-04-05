def format_applications_for_internal_role(data):
    # Create mapping of each parent to its children
    parent_map = {}
    for parent, child in data:
        if parent not in parent_map:
            parent_map[parent] = []
        parent_map[parent].append(child)

    # Identify all children to find root nodes
    all_children = set(child for _, child in data)
    root_nodes = [
        parent for parent in parent_map if parent not in all_children]

    # Track which nodes we've already processed
    processed_nodes = set()

    def build_tree(node_name):
        if node_name in processed_nodes:
            return None  # Skip already processed nodes

        processed_nodes.add(node_name)
        node = {"name": node_name}

        if node_name in parent_map:
            children = []
            for child in parent_map[node_name]:
                child_node = build_tree(child)
                if child_node:  # Only add if not None (not already processed)
                    children.append(child_node)
            if children:  # Only add children if there are any
                node["children"] = children

        return node

    # Build hierarchy starting from root nodes
    hierarchy = []
    for root in root_nodes:
        tree = build_tree(root)
        if tree:  # Only add if not None
            hierarchy.append(tree)

    return hierarchy

