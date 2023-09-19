from PIL import Image


input_img = "corrupted.jpg"

output_img = "output.jpg"

rmove_str = "CORRUPTED"


def remove_str(infile, outfile, delstr):
    try:
        with open(infile, "rb") as f:
            data = f.read()

            delstr = delstr.encode("utf-8")
            
            new_data = data

            start = new_data.find(delstr)
            while start != -1:

                end = start + len(delstr)
                new_data = new_data[:start] + new_data[end:]
                start = new_data.find(delstr)

            with open(outfile, "wb") as new_f:
                new_f.write(new_data)

            print("done")

    except Exception as e:
        print(f"error : {e}")


remove_str(input_img, output_img, rmove_str)

