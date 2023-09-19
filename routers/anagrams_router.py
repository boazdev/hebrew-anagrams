from flask import Blueprint,jsonify,request
from itertools import permutations,combinations
anagrams = Blueprint('anagrams',__name__)

@anagrams.route("/<word>",methods=['GET'])
def get_word_anagrams(word):
    print(f'word to produce anagrams and sub anagrams: {word[::-1]}')
    #print(f'last letter of word is {word[-1]}')
    word_fixed = word[0:-1] + get_fix_end_char(word[-1])
    print(f'word_fixed : {word_fixed}')
    word_lst = list(get_anagrams_and_sub_anagrams(word_fixed))
    return {"words":word_lst}

def get_anagrams_and_sub_anagrams(word):
    anagrams = set()
    
    # Generate all permutations of the word
    word_permutations = [''.join(p) for p in permutations(word)]
    
    # Generate all combinations of the word
    for i in range(2, len(word) + 1):
        word_combinations = [''.join(c) for c in combinations(word, i)]
        word_permutations.extend(word_combinations)
    
    # Add all permutations and combinations to the set
    for perm in word_permutations:
        anagrams.add(perm[0:-1] + get_fix_middle_char(perm[-1]))
    
    return anagrams

def get_fix_middle_char(char):
    hebrew_letter_mapping = {
        'מ': 'ם',
        'נ': 'ן',
        'פ': 'ף',
        'כ': 'ך',
        'צ': 'ץ'
    }
    if char in hebrew_letter_mapping.keys():
        return hebrew_letter_mapping[char]
    else:
        return char
    
def get_fix_end_char(char):
    hebrew_letter_mapping = {
        'ם': 'מ',
        'ן': 'נ',
        'ץ': 'צ',
        'ף': 'פ',
        'ך': 'כ',
}

    if char in hebrew_letter_mapping.keys():
        return hebrew_letter_mapping[char]
    else:
        return char
    
