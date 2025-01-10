import streamlit as st

def main():
    st.title("Простой опросник")
    
    # Добавляем имя пользователя
    name = st.text_input("Как вас зовут?")
    
    # Вопросы с вариантами ответов
    st.subheader("Ответьте на следующие вопросы:")
    
    # Вопрос 1
    question1 = st.radio(
        "Какой ваш любимый язык программирования?",
        ["Python", "JavaScript", "Java", "C++", "Другой"]
    )
    
    # Вопрос 2
    question2 = st.selectbox(
        "Сколько лет вы занимаетесь программированием?",
        ["Менее 1 года", "1-3 года", "3-5 лет", "Более 5 лет"]
    )
    
    # Вопрос 3
    question3 = st.slider(
        "Оцените ваш уровень знаний (от 1 до 10)",
        min_value=1,
        max_value=10
    )
    
    # Дополнительные комментарии
    comments = st.text_area("Оставьте свои комментарии или пожелания")
    
    # Кнопка отправки
    if st.button("Отправить ответы"):
        if name:
            st.success(f"Спасибо за ответы, {name}!")
            st.write("Ваши ответы:")
            st.write(f"Любимый язык программирования: {question1}")
            st.write(f"Опыт программирования: {question2}")
            st.write(f"Самооценка уровня знаний: {question3}")
            if comments:
                st.write(f"Комментарии или пожелания: {comments}")
