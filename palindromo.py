def palindromo(palabra): 
    palabra = palabra.lower()
    palabra = palabra.replace(" ","")
    palabraalreves = palabra[::-1]
    if palabra==palabraalreves:
        return True

    
    
    

    