pattern_union = [
        {'POS' : {'IN' : ['NOUN', 'ADJ', 'VERB', 'ADP', 'DET']}},
        {'POS' : {'IN' : ['NOUN', 'ADJ', 'VERB', 'ADP', 'DET']}},
        {'POS' : {'IN' : ['NOUN', 'ADJ', 'VERB', 'ADP', 'DET']}, 'OP' : '?'},
        {'POS' : {'IN' : ['NOUN', 'ADJ', 'VERB', 'ADP', 'DET']}, 'OP' : '?'},
        {'POS' : {'IN' : ['NOUN', 'ADJ', 'VERB', 'ADP', 'DET']}, 'OP' : '?'},
        {'POS' : {'IN' : ['NOUN', 'ADJ', 'VERB', 'ADP', 'DET']}, 'OP' : '?'},
];
pattern_esp_1 = [
                {'POS' : {'IN' : ['ADP', 'DET', 'PRON']}, 'OP' : '?'},
                {'POS' : {'IN' : ['NOUN', 'ADJ']}}, 
                {'POS' : {'IN' : ['ADP', 'DET', 'PRON']}, 'OP' : '?'},
                {'POS' : {'IN' : ['ADP', 'DET', 'PRON']}, 'OP' : '?'},
                {'POS' : {'IN' : ['NOUN', 'ADJ', 'PROPN']}}, 
                {'POS' : {'IN' : ['ADP', 'DET', 'PRON']}, 'OP' : '?'},
                {'POS' : {'IN' : ['NOUN', 'ADJ']}, 'OP' : '?'}, 
                {'POS' : {'IN' : ['ADP', 'DET', 'PRON','PROPN']}, 'OP' : '?'},
                {'POS' : {'IN' : ['NOUN', 'ADJ']}, 'OP' : '?'}, 
                {'POS' : {'IN' : ['ADP', 'DET', 'PRON','PROPN']}, 'OP' : '?'},
];

pattern_esp_2 = [
                {'POS' : {'IN' : ['NOUN', 'ADJ']}}, 
                {'POS' : {'IN' : ['NOUN', 'ADJ', 'PROPN']}, 'OP' : '?'}, 
];

pattern = [
  # anchor token: founded
  {
    "RIGHT_ID": "founded",
    "RIGHT_ATTRS": {"ORTH": "founded"}
  },
  # founded -> subject
  {
    "LEFT_ID": "founded",
    "REL_OP": ">",
    "RIGHT_ID": "subject",
    "RIGHT_ATTRS": {"DEP": "nsubj"}
  },
  # "founded" follows "initially"
  {
    "LEFT_ID": "founded",
    "REL_OP": ";",
    "RIGHT_ID": "initially",
    "RIGHT_ATTRS": {"ORTH": "initially"}
  }
]
pattern_sin = [
    # anchor token: founded
  {
    "RIGHT_ID": "founded",
    "RIGHT_ATTRS": {"DEP": {'IN' : ["nsubj", "det"]}}
  },
  # founded -> subject
  {
    "LEFT_ID": "founded",
    "REL_OP": ">",
    "RIGHT_ID": "subject",
    "RIGHT_ATTRS": {"DEP": "amod"}
  }
    
]