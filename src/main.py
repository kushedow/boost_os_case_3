from functions import load_data, get_category, get_product


def main():
    data = load_data("products.json")
    print(data)

    print(get_category(data))
    # print(get_product(data))


if __name__ == '__main__':
    main()
