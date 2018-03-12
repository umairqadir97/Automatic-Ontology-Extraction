import nltk
from nltk.parse import stanford

####
def pos_tag(text, simple=False):
    """ Tokenizes a given text and determines the pos-tags. Lowercases
        the text.

     Params:
        text: string to be tokenized
        simple: boolean indicating weather to simplify the pos tags

    Returns:
        list of tuples of form (token, pos-tag)
    """
    tokens = nltk.word_tokenize(text.lower())
    pos = nltk.pos_tag(tokens)
    # simplify tags if requested
    if simple:
        simple_pos = []
        for word, tag in pos:
            new_tag = nltk.tag.mapping.map_tag('en-ptb', 'universal',tag)
            # simplification removes some tags
            # not allowed to use empty tag so use initial one
            if not new_tag:
                new_tag = tag
            simple_pos.append((word, new_tag))
        pos = simple_pos
    return pos


def parse_sentence(sentence, return_dependency=False):
    """
    Input: simple English sentece
    Output: Parse Tree(nltk.tree.Tree) of that sentence
    """
    parser = stanford.StanfordParser()
    tree = list(parser.raw_parse(sentence))

    if return_dependency:
        dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
        tree = [parse.tree() for parse in dep_parser.raw_parse(sentence)]
        return tree[0]
    else:
        print tree[0]
        return tree[0]
