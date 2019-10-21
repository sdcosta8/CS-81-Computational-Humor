

def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    import string

    BONUSFORProperNoun = 1.0
    client = language.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    # get rid of punctation
    textWithNoPun = text_content.translate(str.maketrans('', '', string.punctuation)).split() 

    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)


    output = [] 
    # Loop through entitites returned from the API
    for entity in response.entities:
        score = 0
        if (enums.Entity.Type(entity.type).name) not in ["ADDRESS", "DATE", "PRICE"]:
            
            
            for metadata_name, metadata_value in entity.metadata.items():
                if metadata_name.find("wikipedia") != -1:
                    score = BONUSFORProperNoun + entity.sentiment.magnitude
                    output.append([entity.name, score])
                    continue
        
            
            # Loop over the mentions of this entity in the input document.
            # The API currently supports proper noun mentions.
            for mention in entity.mentions:
                if (enums.EntityMention.Type(mention.type).name) == "PROPER":
                    score = BONUSFORProperNoun + entity.sentiment.magnitude
                    output.append([mention.text.content, score])
                continue
            

            
            if entity.salience > .9:
                score = entity.sentiment.magnitude * entity.sentiment.score
                output.append([entity.name, score])
                continue

            if entity.sentiment.score < -.5 or entity.sentiment.score > .5:
                score = entity.sentiment.magnitude
                output.append([entity.name, score])
                continue

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    return sorted(output,key = lambda x : x[1], reverse=1)

# sample_analyze_entities("The pitbull bit the idiot and ran off. the man ran faster than Usian Bolt and Lebron James. He ran straight to the dog park.")

