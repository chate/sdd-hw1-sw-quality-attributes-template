# Homework #1: Quality Attributes Scenario Analysis

## วัตถุประสงค์
- เข้าใจ Quality Attributes ที่สำคัญในการออกแบบ Software
- ฝึกเขียน Quality Attribute Scenarios ในรูปแบบมาตรฐาน
- วิเคราะห์ระบบจริงด้วยมุมมองของ Software Architect

## งานที่ต้องทำ
จากกิจกรรมที่ทำในห้องเรียน เลือก Quality Attribute Scenarios มา **1 scenario** ที่คิดว่าสำคัญที่สุดสำหรับระบบที่วิเคราะห์ 

## รูปแบบ Quality Attribute Scenario

แต่ละ scenario ต้องมีองค์ประกอบครบ 6 ส่วน:

1. **Attribute**: Quality Attribute ที่เกี่ยวข้อง (เช่น Performance, Availability, Security)
2. **Source**: แหล่งที่มาของ stimulus (ผู้ใช้, ระบบอื่น, administrator, hacker)
3. **Stimulus**: เหตุการณ์ที่เกิดขึ้น
4. **Artifact**: ส่วนของระบบที่ได้รับผลกระทบ
5. **Environment**: สภาวะของระบบขณะเกิดเหตุการณ์
6. **Response**: การตอบสนองที่ต้องการ (วัดได้เป็นตัวเลข)

## ตัวอย่าง Quality Attribute Scenario

### Example: Performance Scenario for Course Registration System

**Attribute**: Performance (Latency)

**Source**: 1,000 นิสิตพร้อมกัน

**Stimulus**: คลิกค้นหารายวิชาที่เปิดสอน

**Artifact**: Database query module และ web server

**Environment**: ช่วง peak time ของการลงทะเบียน (08:00-09:00 AM)

**Response**: ระบบต้องแสดงผลลัพธ์ภายใน 2 วินาที สำหรับ 95% ของ requests

**เขียนเป็นประโยค**: 
"เมื่อมีนิสิต 1,000 คนพร้อมกันค้นหารายวิชาในช่วง peak time ของการลงทะเบียน ระบบต้องแสดงผลลัพธ์ภายใน 2 วินาที สำหรับ 95% ของ requests"

---

## ไฟล์ที่ต้องแก้ไข
แก้ไขไฟล์ `quality_scenarios.md` โดยเขียน scenarios ของคุณลงไป

## การส่งงาน
1. แก้ไขไฟล์ `quality_scenarios.md`
2. กรอกข้อมูลให้ครบถ้วน
3. Commit และ push ขึ้น GitHub
4. ระบบจะตรวจสอบความสมบูรณ์อัตโนมัติ

## เกณฑ์การให้คะแนน

### Auto-grading (35 คะแนน):
- ✅ ไฟล์มีโครงสร้างถูกต้อง: 10 คะแนน
- ✅ กรอกข้อมูลส่วนตัวครบถ้วน: 5 คะแนน
- ✅ scenario มีครบ 6 องค์ประกอบ: 20 คะแนน

### Manual grading (15 คะแนน):
อาจารย์จะให้คะแนนเพิ่มจาก:
- ความเหมาะสมของ scenario กับระบบที่เลือก (5 คะแนน)
- Response ที่วัดได้เป็นตัวเลขชัดเจน (5 คะแนน)
- ความสมจริงและนำไปใช้งานได้ (5 คะแนน)

## Tips
- ใช้ตัวเลขที่สมจริง (เช่น response time, number of users)
- คิดถึง edge cases และ worst-case scenarios
- Response ต้องวัดได้ (measurable) เสมอ
- ครอบคลุมทั้ง normal operation และ error conditions

## กำหนดส่ง
ดูใน GitHub Classroom

---
**Good luck! 🚀**
