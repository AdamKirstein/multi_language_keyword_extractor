# multi_language_keyword_extractor

This is a program that is built on Spacy, utilizing all the available language models within spacy to extract keywords from givent ext. The basic flow of the algorithm is that text will be passed through the script, its language will be detected, if that language has an associated Spacy language model, it will be called and keywords will be extracted. If not, the text will be translated using googletrans, and the keywords will be extracted via the english model. 

# Usage
the output is a pandas dataframe, but can be configured to just be a dictionary. 

the main script takes a dataframe,
column1 = your key column. The initial output is a dict, so this would be a unique row ID that each text-to-be-keyword-extracted will be associated with. 
column2 = the text you want to extract 
new_column = the new column to hold the newly extracted keywords in the resulting output dataframe. 

# importlib

the algorithm uses importlib and subprocess to install each language model without you having to go to your termainl and do it manually. And import lib will read each language model as an import object and import it using spacy's recommended method : 
                                                        
                                                                
                                                          import en_core_web_sm
                                                          nlp = en_core_web_sm.load()
 
 
 learn more here: https://spacy.io/models
 
 
 
 
