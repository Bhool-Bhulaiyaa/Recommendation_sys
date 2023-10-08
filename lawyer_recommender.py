import streamlit as st
import pickle
lawyer_data = pickle.load(open("lawyers_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
lawyer_names = lawyer_data['Rating'].tolist() 
st.header("Lawyer recommender")
selected_lawyer = st.selectbox("Select lawyers you want", lawyer_names)

def recommend(lawyer_data, target_name):
    index = int(lawyer_data[lawyer_data['Name'] == target_name].index[0])
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    store=[]
    for i in distance[0:5]:
        store.append(lawyer_data.iloc[i[0]]['Name'])
    return store

if st.button("Show recommendation"):
    name=recommend(selected_lawyer)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(name[0])
    with col2:
        st.text(name[1])
    with col3:
        st.text(name[2])
    with col4:
        st.text(name[3])
    with col5:
        st.text(name[4])
    st.write("Selected lawyer:", selected_lawyer)
