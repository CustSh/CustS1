document.addEventListener("DOMContentLoaded", function () {
    let page = 2; // Начальная страница
    let isLoading = false;
    const baseUrl = window.baseUrl; // Получаем значение из шаблона

    async function loadMoreProducts() {
        if (isLoading) return;

        isLoading = true;
        document.getElementById("loader").style.display = "block";

        try {
            // Добавляем текущую страницу к базовому URL
            const response = await fetch(`${baseUrl}&page=${page}`, {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            if (response.ok) {
                const data = await response.json();

                const productContainer = document.getElementById("product-list");
                data.products.forEach(product => {
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
                });

                if (data.has_next) {
                    page++;
                } else {
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
            loadMoreProducts();
        }
    }

    window.addEventListener("scroll", handleScroll);
});
