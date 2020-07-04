import spacy
from langdetect import detect
from googletrans import Translator
import importlib
from string import punctuation


def get_keywords(dataframe, column1, column2, new_column):
  
  imports = list(lang_model_keys.models)
  translator = Translator()
  installLangModels(lang_model_keys.models)
  importLangModels(imports)
  
  
  
  extracted_kw_dict = {}
  langs_dict = {}
  keys = list(lang_model_keys.langs)
  for i in range(len(df)):
      langs_dict[df[column1][i]] = detect(df[column2][i]) 
      
      lang_of_item = detect(df[column2][i])
      if lang_of_item in keys:
        print(df[column1][i], ": has a spacy model")
        spacy_model= ''.join(lang_model_keys[lang_model_keys.langs == lang_of_item]['models'].values)
        nlp = eval(spacy_model).load()
        print('loading spacy lang model for:',lang_of_item)
        extracted_kw_dict[df[column1][i]] = extract_keywords(nlp, df[column2][i])
      else:
        try:
          print('no spacy model for: ',df[column1][i])
          nlp = eval('en_core_web_md').load()
          translated_item = translator.translate(df[column2][i]).text
          extracted_kw_dict[df[column1][i]] = extract_keywords(nlp, translated_item)
        except: 
          bad_translated_item = breakup_keyword_df(df[column2][i])
          extracted_kw_dict[df[column1][i]] = extract_keywords(nlp,bad_translated_item)
          
          
  df[new_column] = df[column1].map(extracted_kw_dict)
  df['lang_of_item'] = df[column1].map(langs_dict)
  return df
  
  
  
  
  def breakup_keyword_df(string):
    first_25 = int(len(string)*0.25)
    first_50 = int(len(string)*0.50)
    first_75 = int(len(string)*0.75)




def extract_keywords(nlp, sequence):
    """ Takes a Spacy core language model,
    string sequence of text and optional
    list of special tags as arguments.
    
    If any of the words in the string are 
    in the list of special tags they are immediately 
    added to the result.  
    
    Arguments:
        sequence {str} -- string sequence to have keywords extracted from
    
    Keyword Arguments:
        tags {list} --  list of tags to be automatically added (default: {None})
    
    Returns:
        {list} -- list of the unique keywords extracted from a string
    """    
    result = []

    # custom list of part of speech tags we are interested in
    # we are interested in proper nouns, nouns, and adjectives
    # edit this list of POS tags according to your needs. 
    pos_tag = ['PROPN','NOUN','ADJ']
    # create a spacy doc object by calling the nlp object on the input sequence
    doc = nlp(sequence.lower())
    for chunk in doc.noun_chunks:
        final_chunk = ""
        for token in chunk:
            if (token.pos_ in pos_tag):
                final_chunk =  final_chunk + token.text + " "
        if final_chunk:
            result.append(final_chunk.strip())
    for token in doc:
        if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if (token.pos_ in pos_tag):
            result.append(token.text)
    return list(set(result))
    
    
    
    
 
def importLangModels(imports):
    for lib in imports:
        globals()[lib] = importlib.import_module(lib)
        print("Successfully imported ", lib, '.')

            
            
def installLangModels(lang_model_keys):
    for i in lang_model_keys:
            subprocess.call("python3 -m spacy download {}".format(i),shell=True)
            print("Loaded language vocabularies")  
            
            
            
            
lang_model_keys = {'da': 'da_core_news_md',
                       'nl': 'nl_core_news_md',
                       'en': 'en_core_web_md',
                       'fr': 'fr_core_news_md',
                       'de': 'de_core_news_md',
                       'el': 'el_core_news_md',
                       'it': 'it_core_news_md',
                       'ja': 'ja_core_news_md',
                       'lt': 'lt_core_news_md',
                       'nb': 'nb_core_news_md',
                       'pl': 'pl_core_news_md',
                       'pt': 'pt_core_news_md',
                       'ro': 'ro_core_news_md',
                       'es': 'es_core_news_md',
                       'zh': 'zh_core_web_md'}

lang_model_keys = pd.DataFrame(lang_model_keys, index=[0]).T.reset_index()
lang_model_keys.columns=['langs', 'models']





##### Applying it ##########

df_keywords = get_keywords(df ,column1 = 'key_column_name', column2 ='text_column',new_column='name_of_new_col')
   
