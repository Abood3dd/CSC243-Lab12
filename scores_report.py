import os


def main():
    count = 0

    try:
        with open('scores.txt') as file, open('temp.txt', 'w') as temp, open('pass.txt', 'w') as pass_file:
            for line in file:
                fields = line.rstrip('\n').split(',')
                name = fields[0]
                score_text = fields[1]

                if score_text.isdigit():
                    score = int(score_text)
                    count += 1

                    if name == 'Maya':
                        fields[1] = '88'
                        score = 88
                    if name == 'Karim':
                        print(score)

                    if name != 'Nour':
                        temp.write(','.join(fields) + '\n')
                        if score >= 60:
                            pass_file.write(name + '\n')

            print(count)

        os.remove('scores.txt')
        os.rename('temp.txt', 'scores.txt')
    except FileNotFoundError:
        print('File not found')


if __name__ == "__main__":
    main()

