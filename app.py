import streamlit as st

def create_new_asic():
    st.title("Create new ASIC")
    new_asic_name = st.text_input("Insert new ASIC name")
    if st.button("Run this request"):
        st.success(f"ASIC '{new_asic_name}' created!")

def select_asic():
    st.title("Select ASIC in the list")
    # Dummy list of ASICs
    asic_list = ["ASIC_1", "ASIC_2", "ASIC_3"]
    asic_choice = st.selectbox("ASICs List", asic_list)
    question = st.text_input("Ask Question")
    if st.button("Run this request", key="ask"):
        st.text_area("Answer to Question", "Response to the question asked.", height=300)

def main():
    st.sidebar.title("EMCA Verification AI Tool")
    app_mode = st.sidebar.radio("Choose the option:",
                                ["Create new ASIC", "Select ASIC in the list"])

    if app_mode == "Create new ASIC":
        create_new_asic()
    elif app_mode == "Select ASIC in the list":
        select_asic()

if __name__ == "__main__":
    main()
