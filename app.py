import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Questionnaire Form", layout="centered")
st.title("📋 Questionnaire Form")

# ตัวแปรเก็บข้อมูลที่กรอก
form_data = {}

# --- ฟังก์ชันตัวช่วยสร้าง UI (เทียบเท่า add_item ใน tkinter) ---
def add_item(label, has_input=False, unit="", description=""):
    # สร้าง Checkbox
    is_checked = st.checkbox(label, key=f"chk_{label}")
    user_input = None
    
    # ถ้าถูกติ๊ก ให้แสดงคำอธิบายและช่องกรอกข้อมูล
    if is_checked:
        if description:
            st.caption(f"ℹ️ {description}") # แสดงคำอธิบายสีเทาตัวเล็ก
            
        if has_input:
            # จัด Layout ให้ช่องกรอกข้อมูลและหน่วยอยู่บรรทัดเดียวกัน
            col1, col2 = st.columns([3, 1])
            with col1:
                user_input = st.text_input(f"ระบุ {label}", key=f"txt_{label}", label_visibility="collapsed")
            with col2:
                st.write(unit)
                
    # เก็บข้อมูลลง Dictionary หากมีการติ๊ก
    if is_checked:
        form_data[label] = user_input if has_input else True

# ==========================================
# 1. Overview
# ==========================================
st.header("1. Overview")
st.divider()

st.subheader("Design Party")
design_party = [
    "Interior Designer", "Landscape Designer", "MEP Engineer", 
    "Structure Engineer", "Lighting Designer", "Signage Designer", 
    "EIA Consultant", "Kitchen Laundry Consultant"
]
for item in design_party: 
    add_item(item, description=f"ระบุรายละเอียดของ {item} (ถ้ามี)")

st.subheader("Target Type")
add_item("Corporate Retreat")
add_item("Family(+ Kid clubs)", description="มีพื้นที่รองรับกิจกรรมสำหรับเด็ก")
add_item("Elderly")
add_item("Wellness Seeker")
add_item("Athlete")
add_item("Group Tour")

st.subheader("National (%)")
add_item("Asian (Included Thais)", has_input=True, unit="%", description="ใช้เงิน: 8,700-9,100 อยู่นาน: 3-4วัน")
add_item("Europe", has_input=True, unit="%", description="ใช้เงิน: 50,900 อยู่นาน: 14วัน")
add_item("Middle East", has_input=True, unit="%", description="ใช้เงิน: 88,500 อยู่นาน: 12วัน")
add_item("Chinese", has_input=True, unit="%", description="ใช้เงิน: 49,000 อยู่นาน: 7วัน")

# ==========================================
# 2. Function
# ==========================================
st.header("2. Function")
st.divider()

st.subheader("Wellness & Spa")
st.markdown("**Treatment**")
add_item("Massage")
add_item("Spa Suites")
add_item("Beauty & Grooming")

st.markdown("**Hydrotherapy & Thermal**")
add_item("Hot and Cold plunge")
add_item("Vitality Pool")
add_item("Steam Room")

st.markdown("**Mind and Body**")
mind_body = ["Yoga Area", "Pilates", "Sound Bath", "Fitness", "Hyrox", "Tennis", "Muay Thai"]
for item in mind_body: 
    add_item(item)

st.markdown("**Medical**")
medical = ["Wellness Consult", "IV Drip", "Sleep Therapy", "Hyperbaric Chamber", "Cryotherapy"]
for item in medical: 
    add_item(item)

st.subheader("Food & Beverage")
add_item("All-Day Dining")
add_item("Beach Bar/Pool Bar")
add_item("Fine Dining")
add_item("Specialize Dining")

st.subheader("Event (ตรม.)")
add_item("Ball room", has_input=True, unit="ตรม.")
add_item("Wedding Lawn", has_input=True, unit="ตรม.")
add_item("Workshop Area", has_input=True, unit="ตรม.")

# ==========================================
# 3. Construction
# ==========================================
st.header("3. Construction")
st.divider()

st.subheader("Building")
add_item("อาคารขนาดใหญ่")
add_item("ที่จอดรถใต้ดิน")

st.subheader("Material")
st.markdown("**เกรดวัสดุ**")
add_item("Luxury (หินอ่อน ไม้)")
add_item("Eco (วัสดุทดแทน)")
add_item("Standard")

st.markdown("**สไตล์วัสดุ**")
add_item("วัสดุผิวจริง Raw")
add_item("เรียบหรู Polished")

st.subheader("Sustainability")
add_item("เก็บต้นไม้เดิมที่", has_input=True, unit="%")
add_item("Passive Design")
add_item("Solar Cell ที่", has_input=True, unit="%")
add_item("จัดการน้ำเสีย")
add_item("LEED,TREES")
add_item("Energy Monitor")
add_item("Zero Waste")

# ==========================================
# 4. Management
# ==========================================
st.header("4. Management")
st.divider()

st.subheader("Employee (คน)")
st.markdown("**Front of the house**")
add_item("Bellman", has_input=True, unit="คน")
add_item("Drivers", has_input=True, unit="คน")
add_item("Reception", has_input=True, unit="คน")

st.markdown("**Housekeeping**")
add_item("แม่บ้าน", has_input=True, unit="คน")
add_item("พนักงานทำความสะอาด", has_input=True, unit="คน")
add_item("คนสวน", has_input=True, unit="คน")
add_item("รปภ.", has_input=True, unit="คน")

st.markdown("**F&B and Spa**")
add_item("เชฟ", has_input=True, unit="คน")
add_item("พนักงานเสิร์ฟ", has_input=True, unit="คน")
add_item("นักบำบัด", has_input=True, unit="คน")

st.markdown("**Medical**")
add_item("พยาบาล", has_input=True, unit="คน")
add_item("คุณหมอ", has_input=True, unit="คน")

st.subheader("Back of the house")
add_item("ห้องพักพนักงาน", has_input=True, unit="ระบุกลุ่มพนักงาน", description="ระบุกลุ่มพนักงานที่อนุญาตให้เข้าพัก")
add_item("ระบบซักรีดภายใน")

# ==========================================
# ส่วนแสดงผลด้านล่าง
# ==========================================
st.divider()

# ปุ่มกดยืนยัน (ใช้ type="primary" จะเป็นปุ่มสีเด่น)
if st.button("บันทึก / แสดงข้อมูล", type="primary", use_container_width=True):
    st.success("ระบบได้รับข้อมูลของคุณแล้ว! (ตัวอย่างข้อมูลที่ได้อยู่ด้านล่าง)")
    
    # แสดงข้อมูลที่ผู้ใช้ติ๊กเลือกและกรอกออกมาเป็นก้อนข้อมูล (คล้ายๆ print ใน Console แต่แสดงบนเว็บเลย)
    st.json(form_data)