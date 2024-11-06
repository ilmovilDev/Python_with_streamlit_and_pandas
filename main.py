# main.py
import streamlit as st
import pandas as pd
import plotly.express as px


def show_tabela():
    st.set_page_config(layout="wide")
    # df_reviews = pd.read_csv("datasets/customer reviews.csv")
    df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

    price_max = df_top100_books["book price"].max()
    price_min = df_top100_books["book price"].min()

    max_price = st.sidebar.slider(
        "Price Range", price_min, price_max, price_max)

    st.write("Top 100 Trending Books")
    df_book = df_top100_books[df_top100_books["book price"] <= max_price]
    st.dataframe(df_book)

    left_figure = px.bar(df_book["year of publication"].value_counts())
    right_figure = px.histogram(df_book["book price"])

    col1, col2 = st.columns(2)

    col1.plotly_chart(left_figure)
    col2.plotly_chart(right_figure)


def main():
    show_tabela()


if __name__ == "__main__":
    main()
