from PIL import Image, ImageFilter 
  
image = Image.open(r"teste.jpeg") 
image = image.convert("L") 
image = image.filter(ImageFilter.FIND_EDGES) 
image.save(r"borda.png")