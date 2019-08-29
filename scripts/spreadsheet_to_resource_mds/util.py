#! /usr/bin/python3
#-*- coding: UTF-8 -*-
import re
import unidecode

from goose3 import Goose

GRAB_FIRST_TWO_SENTENCES_RE = '[.!?][\s]{1,2}(?=[A-Z])'
REMOVE_SPECIAL_CHARACTERS_RE = '[^A-Za-z0-9]+'
REMOVE_SPECIAL_CHARACTERS_KEEP_DASHES_RE = '[^A-Za-z0-9-]+'

CLOSE_PAREN = ")"
COLON = "&#58"
COMMA = ","
DASH = "-"
EMPTY = ""
MARKDOWN_SUFFIX = ".md"
OPEN_PAREN = "("
PERIOD = "."
QUOTE = "\""
UNDERSCORE = "_"
SPACE = " "

def get_excerpt_from_page(url):
    """ Rudimentary excerpt creator."""
    try:
        regex_object = re.compile(GRAB_FIRST_TWO_SENTENCES_RE)
        all_text_on_page = Goose().extract(url=url).cleaned_text if url != EMPTY else EMPTY
        sentences = regex_object.split(all_text_on_page, re.UNICODE)
    except:
        return EMPTY

    if len(sentences) == 0 or _is_common_bad_excerpt(sentences[0]):
        return EMPTY
    if len(sentences) == 1:
        return _cleanup_excerpt(sentences[0] + PERIOD.replace(COLON, EMPTY))
    else:
        return _cleanup_excerpt((sentences[0] + PERIOD + SPACE + sentences[1] + PERIOD).replace(COLON, EMPTY))

def _cleanup_excerpt(str):
    return " ".join(str.split()).replace(COLON, EMPTY).replace(":", "")

def _is_common_bad_excerpt(sentence):
    common_bad_excerpts = [
        "JavaScript isn't enabled in your browser",
        "Get YouTube without the ads",
    ]
    for excerpt in common_bad_excerpts:
        if excerpt in sentence:
            return True
    return False

def title_to_file_path(title, resource_type):
    resources_folder_path = "../../collections/_"
    resources_folder_path = resources_folder_path + resource_type + "/"

    if title == EMPTY or title == UNDERSCORE:
        return EMPTY
    return "{}{}{}".format(
            resources_folder_path,
            _camel_case_to_dashed(_remove_extraneous_symbols(title.replace("58", ""))),
            MARKDOWN_SUFFIX)

def author_to_file_path(valid_author_slug):
    """ Replaces extraneous symbols and cleans up accents and umlauts
        in author names. """
    if valid_author_slug == EMPTY or valid_author_slug == UNDERSCORE:
        return EMPTY
    return "{}{}{}".format(
        "../../collections/_authors/",
        valid_author_slug,
        MARKDOWN_SUFFIX)

def get_valid_author_slug(author):
    return _remove_extraneous_symbols_keep_dashes(unidecode.unidecode(
        re.sub(UNDERSCORE, DASH, re.sub(SPACE, DASH, author.strip().lower()))))

def _camel_case_to_dashed(title):
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2',
        re.sub('(.)([A-Z][a-z]+)',r'\1-\2', title)).lower()

def _remove_extraneous_symbols(str):
    return _remove_extraneous_symbols_with_regex(
        str, REMOVE_SPECIAL_CHARACTERS_RE)

def _remove_extraneous_symbols_keep_dashes(str):
    return _remove_extraneous_symbols_with_regex(
        str, REMOVE_SPECIAL_CHARACTERS_KEEP_DASHES_RE)

def _remove_extraneous_symbols_with_regex(str, regex):
    str = _replace_apostrophe_char_with_char(['s', 'S', 't', 'T'], str)
    return re.sub(
        '-+',
        '-',
        re.sub(regex, EMPTY, str))

def _replace_apostrophe_char_with_char(chars, str):
    for char in chars:
        str = re.sub(r"(\w+)'{}".format(char), r'\1{}'.format(char.lower()), str)
    return str
