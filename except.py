while True:
    try:
        n = int(input('Enter a number'))
        print(16/n)
        break
    except ValueError:
        print("Oops You got Error!")
    except ZeroDivisionError:
        print("Zero cant be used")
    except:
        break


