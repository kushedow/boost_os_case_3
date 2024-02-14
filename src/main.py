from functions import load_data, get_category_and_product


def main():
    data = load_data("products.json")
    get_category_and_product(data)
    # print(get_product(data))


if __name__ == '__main__':
    main()
