from array_stack import ArrayStack


def is_matched_html(raw):
    stack = ArrayStack()
    j = raw.find('<')

    while j != -1:
        k = raw.find('>', j+1)  # find next '>'
        if k == -1:
            return False

        tag = raw[j+1:k]  # < > 之间的内容
        if not tag.startswith('/'):  # it's a opening tag
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False  # mismatched delimiter

        j = raw.find('<', k+1)

    return stack.is_empty()


if __name__ == '__main__':
    raw = '<body><center><h1> The Little Boat </h1></center><p> The storm ' \
          'tossed the littleboat like a cheap sneaker in anold washing machine. ' \
          'The threedrunken fishermen were used tosuch treatment, of course, ' \
          'butnot the tree salesman, who even asa stowaway now felt that hehad ' \
          'overpaid for the voyage. </p><ol><li> Will the salesman die? </li>' \
          '<li> What color is the boat? </li><li> And what about Naomi? ' \
          '</li></ol></body>'
    print(is_matched_html(raw))