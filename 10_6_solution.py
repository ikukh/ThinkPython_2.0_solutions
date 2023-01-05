
"""
Exercise 10-6.
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are
anagrams.
"""

def anagram(s1,s2):

    # Prerearing given words to get all of them as lowercase without spases 
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    original_s12 = (sorted(s2))

    # Sort symbols 
    s11=(sorted(s1))
    s12=(sorted(s2))

    ww=[]
    
    # Comparing given words
    for w1 in s11:
        for w2 in s12:
            if w2 == w1:
                """
                When we are getting the same letters we don't need to compare it anymore,
                so we can delete it from the original line
                """
                s12.remove(w2)
                ww.append(w2)

    if original_s12 == ww:
        print('Given words are anagrams')
    else: 
        print('Words are not anagrams')

anagram('Exeptions', 'note')