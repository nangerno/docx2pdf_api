import convertapi
convertapi.api_secret = 'nKw9vFyQzRJzoVLC'
convertapi.convert('pdf', {
    'File': 'resume.docx'
}, from_format = 'docx').save_files('output.pdf')