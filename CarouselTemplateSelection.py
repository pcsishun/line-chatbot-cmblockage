from linebot.models import *
from linebot import *
import json 

def templateCount_1(data):
    print(data)

    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]     

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    )
                ]
            )
        )
    return carousel_template_message

def templateCount_2(data):


    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]


    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_3(data):

    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_4(data):
    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    blk_code3 = data[3][0]
    blk_id3 = data[3][1]
    blk_img3 = data[3][2]
    longitude3 =data[3][3]# หลัง 
    latitude3 = data[3][4] # ขึ้นก่อน 
    blk_address3 = data[3][5]

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img3),
                    title= blk_address3,
                    text= blk_code3, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude3, longitude3)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id3)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_5(data):

    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    blk_code3 = data[3][0]
    blk_id3 = data[3][1]
    blk_img3 = data[3][2]
    longitude3 =data[3][3]# หลัง 
    latitude3 = data[3][4] # ขึ้นก่อน 
    blk_address3 = data[3][5]

    blk_code4 = data[4][0]
    blk_id4 = data[4][1]
    blk_img4 = data[4][2]
    longitude4 =data[4][3]# หลัง 
    latitude4 = data[4][4] # ขึ้นก่อน 
    blk_address4 = data[4][5]
    
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img3),
                    title= blk_address3,
                    text= blk_code3, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude3, longitude3)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id3)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img4),
                    title= blk_address4,
                    text= blk_code4, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude4, longitude4)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id4)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_6(data):

    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    blk_code3 = data[3][0]
    blk_id3 = data[3][1]
    blk_img3 = data[3][2]
    longitude3 =data[3][3]# หลัง 
    latitude3 = data[3][4] # ขึ้นก่อน 
    blk_address3 = data[3][5]

    blk_code4 = data[4][0]
    blk_id4 = data[4][1]
    blk_img4 = data[4][2]
    longitude4 =data[4][3]# หลัง 
    latitude4 = data[4][4] # ขึ้นก่อน 
    blk_address4 = data[4][5]

    blk_code5 = data[5][0]
    blk_id5 = data[5][1]
    blk_img5 = data[5][2]
    longitude5 =data[5][3]# หลัง 
    latitude5 = data[5][4] # ขึ้นก่อน 
    blk_address5 = data[5][5]


    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img3),
                    title= blk_address3,
                    text= blk_code3, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude3, longitude3)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id3)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img4),
                    title= blk_address4,
                    text= blk_code4, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude4, longitude4)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id4)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img5),
                    title= blk_address5,
                    text= blk_code5, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude5, longitude5)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id5)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_7(data):

    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    blk_code3 = data[3][0]
    blk_id3 = data[3][1]
    blk_img3 = data[3][2]
    longitude3 =data[3][3]# หลัง 
    latitude3 = data[3][4] # ขึ้นก่อน 
    blk_address3 = data[3][5]

    blk_code4 = data[4][0]
    blk_id4 = data[4][1]
    blk_img4 = data[4][2]
    longitude4 =data[4][3]# หลัง 
    latitude4 = data[4][4] # ขึ้นก่อน 
    blk_address4 = data[4][5]

    blk_code5 = data[5][0]
    blk_id5 = data[5][1]
    blk_img5 = data[5][2]
    longitude5 =data[5][3]# หลัง 
    latitude5 = data[5][4] # ขึ้นก่อน 
    blk_address5 = data[5][5]

    blk_code6 = data[6][0]
    blk_id6 = data[6][1]
    blk_img6 = data[6][2]
    longitude6 =data[6][3]# หลัง 
    latitude6 = data[6][4] # ขึ้นก่อน 
    blk_address6 = data[6][5]

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img3),
                    title= blk_address3,
                    text= blk_code3, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude3, longitude3)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id3)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img4),
                    title= blk_address4,
                    text= blk_code4, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude4, longitude4)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id4)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img5),
                    title= blk_address5,
                    text= blk_code5, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude5, longitude5)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id5)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img6),
                    title= blk_address6,
                    text= blk_code6, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude6, longitude6)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id6)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_8(data):

    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    blk_code3 = data[3][0]
    blk_id3 = data[3][1]
    blk_img3 = data[3][2]
    longitude3 =data[3][3]# หลัง 
    latitude3 = data[3][4] # ขึ้นก่อน 
    blk_address3 = data[3][5]

    blk_code4 = data[4][0]
    blk_id4 = data[4][1]
    blk_img4 = data[4][2]
    longitude4 =data[4][3]# หลัง 
    latitude4 = data[4][4] # ขึ้นก่อน 
    blk_address4 = data[4][5]

    blk_code5 = data[5][0]
    blk_id5 = data[5][1]
    blk_img5 = data[5][2]
    longitude5 =data[5][3]# หลัง 
    latitude5 = data[5][4] # ขึ้นก่อน 
    blk_address5 = data[5][5]

    blk_code6 = data[6][0]
    blk_id6 = data[6][1]
    blk_img6 = data[6][2]
    longitude6 =data[6][3]# หลัง 
    latitude6 = data[6][4] # ขึ้นก่อน 
    blk_address6 = data[6][5]

    blk_code7 = data[7][0]
    blk_id7 = data[7][1]
    blk_img7 = data[7][2]
    longitude7 =data[7][3]# หลัง 
    latitude7 = data[7][4] # ขึ้นก่อน 
    blk_address7 = data[7][5]

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img3),
                    title= blk_address3,
                    text= blk_code3, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude3, longitude3)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id3)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img4),
                    title= blk_address4,
                    text= blk_code4, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude4, longitude4)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id4)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img5),
                    title= blk_address5,
                    text= blk_code5, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude5, longitude5)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id5)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img6),
                    title= blk_address6,
                    text= blk_code6, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude6, longitude6)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id6)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img7),
                    title= blk_address7,
                    text= blk_code7, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude7, longitude7)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id7)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_9(data):

    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    blk_code3 = data[3][0]
    blk_id3 = data[3][1]
    blk_img3 = data[3][2]
    longitude3 =data[3][3]# หลัง 
    latitude3 = data[3][4] # ขึ้นก่อน 
    blk_address3 = data[3][5]

    blk_code4 = data[4][0]
    blk_id4 = data[4][1]
    blk_img4 = data[4][2]
    longitude4 =data[4][3]# หลัง 
    latitude4 = data[4][4] # ขึ้นก่อน 
    blk_address4 = data[4][5]

    blk_code5 = data[5][0]
    blk_id5 = data[5][1]
    blk_img5 = data[5][2]
    longitude5 =data[5][3]# หลัง 
    latitude5 = data[5][4] # ขึ้นก่อน 
    blk_address5 = data[5][5]

    blk_code6 = data[6][0]
    blk_id6 = data[6][1]
    blk_img6 = data[6][2]
    longitude6 =data[6][3]# หลัง 
    latitude6 = data[6][4] # ขึ้นก่อน 
    blk_address6 = data[6][5]

    blk_code7 = data[7][0]
    blk_id7 = data[7][1]
    blk_img7 = data[7][2]
    longitude7 =data[7][3]# หลัง 
    latitude7 = data[7][4] # ขึ้นก่อน 
    blk_address7 = data[7][5]

    blk_code8 = data[8][0]
    blk_id8 = data[8][1]
    blk_img8 = data[8][2]
    longitude8 =data[8][3]# หลัง 
    latitude8 = data[8][4] # ขึ้นก่อน 
    blk_address8 = data[8][5]

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img3),
                    title= blk_address3,
                    text= blk_code3, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude3, longitude3)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id3)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img4),
                    title= blk_address4,
                    text= blk_code4, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude4, longitude4)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id4)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img5),
                    title= blk_address5,
                    text= blk_code5, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude5, longitude5)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id5)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img6),
                    title= blk_address6,
                    text= blk_code6, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude6, longitude6)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id6)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img7),
                    title= blk_address7,
                    text= blk_code7, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude7, longitude7)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id7)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img8),
                    title= blk_address8,
                    text= blk_code8, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude8, longitude8)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id8)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message

def templateCount_10(data):
    
    blk_code = data[0][0]
    blk_id = data[0][1]
    blk_img = data[0][2]
    longitude =data[0][3]# หลัง 
    latitude = data[0][4] # ขึ้นก่อน 
    blk_address = data[0][5]
    
    blk_code1 = data[1][0]
    blk_id1 = data[1][1]
    blk_img1 = data[1][2]
    longitude1 =data[1][3]# หลัง 
    latitude1 = data[1][4] # ขึ้นก่อน 
    blk_address1 = data[1][5]

    blk_code2 = data[2][0]
    blk_id2 = data[2][1]
    blk_img2 = data[2][2]
    longitude2 =data[2][3]# หลัง 
    latitude2 = data[2][4] # ขึ้นก่อน 
    blk_address2 = data[2][5]

    blk_code3 = data[3][0]
    blk_id3 = data[3][1]
    blk_img3 = data[3][2]
    longitude3 =data[3][3]# หลัง 
    latitude3 = data[3][4] # ขึ้นก่อน 
    blk_address3 = data[3][5]

    blk_code4 = data[4][0]
    blk_id4 = data[4][1]
    blk_img4 = data[4][2]
    longitude4 =data[4][3]# หลัง 
    latitude4 = data[4][4] # ขึ้นก่อน 
    blk_address4 = data[4][5]

    blk_code5 = data[5][0]
    blk_id5 = data[5][1]
    blk_img5 = data[5][2]
    longitude5 =data[5][3]# หลัง 
    latitude5 = data[5][4] # ขึ้นก่อน 
    blk_address5 = data[5][5]

    blk_code6 = data[6][0]
    blk_id6 = data[6][1]
    blk_img6 = data[6][2]
    longitude6 =data[6][3]# หลัง 
    latitude6 = data[6][4] # ขึ้นก่อน 
    blk_address6 = data[6][5]

    blk_code7 = data[7][0]
    blk_id7 = data[7][1]
    blk_img7 = data[7][2]
    longitude7 =data[7][3]# หลัง 
    latitude7 = data[7][4] # ขึ้นก่อน 
    blk_address7 = data[7][5]

    blk_code8 = data[8][0]
    blk_id8 = data[8][1]
    blk_img8 = data[8][2]
    longitude8 =data[8][3]# หลัง 
    latitude8 = data[8][4] # ขึ้นก่อน 
    blk_address8 = data[8][5]

    blk_code9 = data[9][0]
    blk_id9 = data[9][1]
    blk_img9 = data[9][2]
    longitude9 =data[9][3]# หลัง 
    latitude9 = data[9][4] # ขึ้นก่อน 
    blk_address9 = data[9][5]

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img),
                    title= blk_address,
                    text= blk_code, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                            )
                        ]
                    ),
                    ### ข้อมูลทั่วไป
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img1),
                    title= blk_address1,
                    text= blk_code1, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude1, longitude1)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id1)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img2),
                    title= blk_address2,
                    text= blk_code2, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude2, longitude2)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id2)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img3),
                    title= blk_address3,
                    text= blk_code3, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude3, longitude3)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id3)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img4),
                    title= blk_address4,
                    text= blk_code4, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude4, longitude4)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id4)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img5),
                    title= blk_address5,
                    text= blk_code5, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude5, longitude5)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id5)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img6),
                    title= blk_address6,
                    text= blk_code6, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude6, longitude6)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id6)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img7),
                    title= blk_address7,
                    text= blk_code7, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude7, longitude7)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id7)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img8),
                    title= blk_address8,
                    text= blk_code8, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude8, longitude8)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id8)
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/{}'.format(blk_img9),
                    title= blk_address9,
                    text= blk_code9, 
                    actions=[
                        URIAction(
                            label='ตำเเหน่ง', 
                            uri='https://www.google.co.th/maps/place/{},{}'.format(latitude9, longitude9)  
                            ),
                        URIAction(
                            label='รายละเอียด',
                            uri='https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id9)
                            )
                        ]
                    ),
                ]
            )
        )
    return carousel_template_message