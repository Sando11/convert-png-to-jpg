from PIL import Image
import os

def converter_imagens(input_folder):
    try:
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(".png"):
                input_path = os.path.join(input_folder, filename)
                imagem = Image.open(input_path)
                output_path = os.path.splitext(input_path)[0] + '.jpg'
                imagem.convert("RGB").save(output_path, "JPEG")
                print(f'Imagem convertida com sucesso: {output_path}')
    except Exception as e:
        print(f'Erro ao converter imagens: {e}')

def main():
    #Digite o caminho da sua pasta com as imagens abaixo
    #write the path your images folder below
    input_folder = ""

    if not os.path.isdir(input_folder):
        print("Pasta inválida.")
        return

    converter_imagens(input_folder)

if __name__ == "__main__":
    main()
