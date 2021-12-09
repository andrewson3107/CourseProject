import re
#TODO: Create parser with following functionality:
# Remove all non alphabet characters
# Remove words less than 2 letters
# Remove show more show less lines
# Remove any links
# Write to updated file

def lower_case(document):
    document = document.lower()
    return document.lower()


def remove_links(document):
    document = re.sub(r'^https?:\/\/.*[\r\n]*', '', document, flags=re.MULTILINE)
    return document


# https://stackoverflow.com/questions/55902042/python-keep-only-alphanumeric-and-space-and-ignore-non-ascii
def remove_non_alpha(document):
    return re.sub("[^0-9a-zA-Z+#' ]+", ' ', document)


def remove_short_words(document):
    document = re.sub(r'\b\w{1,2}\b', '', document)
    return document


def correct_spaces(document):
    document = re.sub(' +', ' ', document)
    return document


def write_to_file(documents):
    f = open('../data/formatted/documents.txt', 'w', encoding='utf-8')
    for document in documents:
        f.write(f'{document}')
        f.write('\n')
    f.close()


def read_documents():
    documents = []
    f = open('../data/raw/scraped_text.txt', 'r', encoding='utf-8')

    temp = f.readlines()
    for i in range(25):
        documents.append(temp[i*9])

    f.close()
    return documents

######################################################################
documents = read_documents()

i = 0
for document in documents:
    document = lower_case(document)
    document = remove_links(document)
    document = remove_non_alpha(document)
    # document = remove_short_words(document)
    document = correct_spaces(document)
    documents[i] = document
    i += 1

write_to_file(documents)