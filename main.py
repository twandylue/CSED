import sys
import trainer
import predictor


def promp_usage():
    print("Usage: python main.py [SUBCOMMAND] [OPTIONS]")
    print("Subcommands and options:")
    print(
        "     -t, --train <file>                    train the model using the <file> (.csv)"
    )
    print(
        "     -p, --predict <file>                  predict the class of the emails in the <file> (.txt)"
    )
    print("     -h, --help                            display this help message")


if __name__ == "__main__":
    # CLI arguments
    if "-h" in sys.argv or "--help" in sys.argv:
        promp_usage()
        sys.exit(0)
    sub_command: str = sys.argv[1]
    if sub_command == "-train" or sub_command == "-t":
        try:
            file_name: str = sys.argv[2]
            # check the file type is .csv
            if file_name.split(".")[-1] != "csv":
                raise Exception("Invalid file type. Please provide a .csv file")
            with open(file_name, "r") as file:
                trainer.train_by_naive_bayes(file_name)
        except IndexError:
            print("Error: File name not provided")
            promp_usage()
            sys.exit(1)
        except FileNotFoundError:
            print(f"Error: File: {file_name} not found")
            promp_usage()
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        sys.exit(0)
    elif sub_command == "-predict" or sub_command == "-p":
        try:
            file_name: str = sys.argv[2]
            # check the file type is .txt
            if file_name.split(".")[-1] != "txt":
                raise Exception("Invalid file type. Please provide a .txt file")
            with open(file_name, "r") as file:
                # read the whole .txt file
                email = file.readlines()
                # concatenate the emails into a single string
                input: str = "".join(email)
                print("Email content:")
                print(input)
                predictor.predict_by_naive_bayes([input])
        except IndexError:
            print("File name not provided")
            promp_usage()
            sys.exit(1)
        except FileNotFoundError:
            print(f"File: {file_name} not found")
            promp_usage()
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        sys.exit(0)
    print("Invalid command")
    promp_usage()
    sys.exit(1)
