#include <iostream>

int main() {
    // Пример приветствия
    std::cout << "Привет, мир!" << std::endl;

    // Пример работы с переменными
    int x = 5;
    int y = 3;
    int sum = x + y;
    std::cout << "Сумма чисел " << x << " и " << y << " равна " << sum << std::endl;

    // Пример работы с условиями
    if (x > y) {
        std::cout << "Число " << x << " больше, чем " << y << std::endl;
    } else {
        std::cout << "Число " << y << " больше, чем " << x << std::endl;
    }

    // Пример работы с циклами
    for (int i = 0; i < 5; ++i) {
        std::cout << "Текущее значение переменной i: " << i << std::endl;
    }

    // Пример работы с массивами
    int arr[5] = {1, 2, 3, 4, 5};
    std::cout << "Элементы массива: ";
    for (int i = 0; i < 5; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
