"""Postorder traversal"""


def disk_space(t, p):
    subtotal = p.element().space()
    for c in t.children(p):
        subtotal += disk_space(t, c)
    return subtotal
