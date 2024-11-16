document.addEventListener("DOMContentLoaded", function () {
    let page = 2; // Начальная страница
    let isLoading = false;
    const baseUrl = window.baseUrl; // Получаем значение из шаблона

    async function loadMoreProducts() {
        if (isLoading) {
            console.log("Загрузка уже идет, запрос пропущен.");
            return;
        }

        isLoading = true;
        document.getElementById("loader").style.display = "block";
        console.log(`Запрос на страницу ${page} отправлен.`);

        try {
            const response = await fetch(`${baseUrl}&page=${page}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            if (response.ok) {
                const data = await response.json();
                console.log("Ответ с сервера получен:", data);

                if (!data.products || data.products.length === 0) {
                    console.warn("Продукты отсутствуют в ответе сервера.");
                }

                const productContainer = document.getElementById("product-list");
                const existingProducts = Array.from(productContainer.querySelectorAll(".card"))
                    .map(card => card.querySelector(".product-name").textContent);

                console.log("Уже существующие товары:", existingProducts);

                data.products.forEach(product => {
                    if (existingProducts.includes(product.name)) {
                        console.warn(`Товар "${product.name}" уже добавлен, пропускаем.`);
                        return;
                    }

                    const productElement = document.createElement("div");
                    productElement.className = "card";
                    productElement.innerHTML = `
                        <div class="card-image-wrapper">
                            ${product.image_url ? `<img src="${product.image_url}" alt="${product.name}">` : ""}
                        </div>
                        <div class="product-name">${product.name}</div>
                        <div class="product-price">${product.price} $</div>
                        <a href="/catalog/${product.slug}" class="card-button">Подробнее</a>
                    `;
                    productContainer.appendChild(productElement);
                    console.log(`Товар "${product.name}" добавлен.`);
                });

                if (data.has_next) {
                    page++;
                    console.log(`Следующая страница: ${page}`);
                } else {
                    console.log("Больше страниц нет, снимаем обработчик прокрутки.");
                    window.removeEventListener("scroll", handleScroll);
                }
            } else {
                console.error("Ошибка загрузки товаров:", response.statusText);
            }
        } catch (error) {
            console.error("Ошибка загрузки товаров:", error);
        } finally {
            isLoading = false;
            document.getElementById("loader").style.display = "none";
        }
    }

    function handleScroll() {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
            console.log("Срабатывает событие прокрутки.");
            loadMoreProducts();
        }
    }

    window.addEventListener("scroll", handleScroll);
});
