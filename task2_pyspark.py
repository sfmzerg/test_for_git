from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit


def get_products_with_categories(products_df: DataFrame,
                                 categories_df: DataFrame,
                                 product_category_links_df: DataFrame) -> DataFrame:
    """
    Возвращает датафрейм со всеми парами "Продукт-Категория" и продуктами без категорий

    Параметры:
    products_df - датафрейм продуктов с колонками: product_id, product_name
    categories_df - датафрейм категорий с колонками: category_id, category_name
    product_category_links_df - датафрейм связей продуктов и категорий с колонками: product_id, category_id

    Возвращает:
    Датафрейм с колонками: product_name, category_name
    """
    # Соединяем продукты с их категориями через таблицу связей
    products_with_categories = (
        products_df.join(
            product_category_links_df,
            "product_id",
            "left"
        )
        .join(
            categories_df,
            "category_id",
            "left"
        )
        .select(
            col("product_name"),
            col("category_name")
        )
    )

    # Добавляем маркер для продуктов без категорий
    result_df = products_with_categories.withColumn(
        "category_name",
        col("category_name")
    )

    return result_df