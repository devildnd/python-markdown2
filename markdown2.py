def markdown(text):
    # Basic markdown implementation (for demonstration)
    return text.replace('# ', '<h1>').replace('#', '</h1>').replace('*', '<strong>').replace('*', '</strong>')
