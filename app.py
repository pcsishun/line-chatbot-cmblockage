import os
from flask import Flask, request
from datetime import datetime
from linebot.models import *
from linebot import *
import json
import requests
from array import*
import CarouselTemplateSelection as CT

# note 
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')



line_bot_api = LineBotApi('')
handler = WebhookHandler('')  # Line Channel secret

##########################
##########################
##########################

# check for existing richmenu
# rich_menu_list = line_bot_api.get_rich_menu_list()
# if not rich_menu_list:
#     result = linebot.richmenu.createRichmeu()
#     if not result:
#         reply.reply_message(event, config.FAILED)


########################### 
# Json without dialogflow #
###########################


@app.route("/callback", methods=['POST'])
def callback():


    menu_list = ['answerSheet','FAQ_answerSheet','พื้นที่รับน้ำ', 'ข้อมูลสิ่งกีดขวาง','active_chatbot','เลือกสถานที่', 'blockages_location','เเจ้งปัญหา','blk_id','คลังความรู้',
                'แก้ไขปัญหาเบื้องต้น','ตัวอย่างเเบบสำรวจ','กรอกข้อมูลเเบบสำรวจ','ข้อสงสัยเเบบสำรวจ','สิ่งกีดขวางรายตำบล','สิ่งกีดขวางรายอำเภอ','เรียกใช้ข้อมูลสิ่งขีดขวาง','คู่มือแก้ปัญหาสิ่งกีดขวางลำน้ำ']   

#  ,'Facebook','website','ที่อยู่'
    body = request.get_data(as_text=True)
    req = request.get_json(silent=True, force=True)
    print(req)

    event_type = req['events'][0]['message']['type']
    replyToken = req['events'][0]['replyToken']
    userid = req['events'][0]['source']['userId']
    # disname = line_bot_api.get_profile(id).display_name

    print('Event type: ', event_type, '\n')
    # print('replyToken: ', replyToken, '\n')
    # print('userid: ', userid, '\n')
    # print('disname: ',disname , '\n')

    #################################
    ###        Menu Starter       ###
    #################################

    # ถ้ามีการรับคำสั่ง Hi, hi, เริ่มต้นจะทำการเข้า menu #
    if event_type == "text":
        text_message = req['events'][0]['message']['text']
        if text_message == "Hi" or text_message == "hi" or text_message == "เริ่มต้น" or text_message == "สวัสดีค่ะ" or text_message == "เรียกใช้ข้อมูลสิ่งขีดขวาง":
            menu_card(replyToken)

        ### เเบบสอบถาม ###
        elif text_message == "ตัวอย่างเเบบสำรวจ": ## ตัวอย่างเเบบสำรวจ !!!
            text_re = "ex_answersheet"
            responseText(replyToken, text_re)

        elif text_message == "กรอกข้อมูลเเบบสำรวจ":
            text_re = "answerSheet"
            responseText(replyToken, text_re)

        ### ข้อมูลทั่วไป ###
        elif text_message == "ข้อมูลสิ่งกีดขวาง":
            text_re = "ข้อมูลสิ่งกีดขวาง"
            responseText(replyToken, text_re)

        elif text_message == "สิ่งกีดขวางใกล้ฉัน":
            text_re = "สิ่งกีดขวางใกล้ฉัน"
            responseText(replyToken, text_re)

        elif text_message == "พื้นที่รับน้ำ":
            text_re = "พื้นที่รับน้ำ"
            responseText(replyToken, text_re)

        elif text_message == "คู่มือแก้ปัญหาสิ่งกีดขวางลำน้ำ":
            text_re = "คู่มือแก้ปัญหาสิ่งกีดขวางลำน้ำ"
            responseText(replyToken, text_re)

        elif text_message == "เเจ้งปัญหา":
            text_re = "reportProblem" #กรุณาส่ง อำเภอ ตำบล
            responseText(replyToken, text_re)


        elif text_message == "ข้อสงสัยเเบบสำรวจ":
            text_re = "active_chatbot"
            responseText(replyToken, text_re)     
 

        elif text_message == "เลือกสถานที่":
            text_re = "เลือกสถานที่"
            responseText(replyToken, text_re)     

        elif text_message == "สิ่งกีดขวางรายตำบล":
            text_re = "สิ่งกีดขวางรายตำบล"
            responseText(replyToken, text_re)  

        elif text_message == "สิ่งกีดขวางรายอำเภอ":
            text_re = "สิ่งกีดขวางรายอำเภอ"
            responseText(replyToken, text_re)  

    #################################
    ### Menu condition management ###
    #################################

    if event_type == "text" or event_type == "message":

        text_message = req['events'][0]['message']['text']

        ## Check log user if not exist begin collect log ##
        ## use this code when you need to update log (not wish to insert) ##
        # user_exsit = count_log_function(userid)
        # user_exsit = int(user_exsit)
        # print('Count user', user_exsit, '\n')

        stamp_time = datetime.now()
        # print('time stamp = ', stamp_time)

        for iter_array in menu_list:
            if iter_array == text_message:
                log_selection(userid, event_type, text_message,stamp_time)


    # Ref to API that are location:
    if event_type == "location":
        text_menu_api = api_selection(userid)
        # print('API menu selection = ', text_menu_api)
        latitude = req['events'][0]['message']['latitude']
        longitude = req['events'][0]['message']['longitude']
        # print('latitude: ', latitude, '\n')
        # print('longitude: ', longitude, '\n')



        if text_menu_api == "ข้อมูลสิ่งกีดขวาง":
            reply_location(latitude, longitude, replyToken, text_menu_api)

    # Ref to API that not location:
    if event_type == "text":

        text_message = req['events'][0]['message']['text']
        text_menu_api = api_selection(userid)
        # print('API menu selection text = ', text_menu_api)
        reply_text(text_menu_api, text_message, replyToken)

    return 'OK'

#########################################################################
########################  Function Menu management ######################
#########################################################################

###########################
### insert log function ###
###########################


def log_selection(id_user, type_msg, text_msg, stamp_time):
    insert_log = requests.get(
        'https://cmblockage.cmfightflood.com/api_selection/{}/{}/{}/{}'.format(id_user, type_msg, text_msg, stamp_time))



def api_selection(id_user):
    text_file = requests.get('https://cmblockage.cmfightflood.com/menu_selection/{}'.format(id_user))
    json_data = json.loads(text_file.text)
    data = json_data[0]['text_msg']
    return data

#########################################################################
#######                          Menu Card                      #########
#########################################################################


def responseText(replytoken, text_re):
    if text_re == "answerSheet":
        text_message = TextSendMessage("ลิงก์เเบบสอบถาม: https://cmblockage.cmfightflood.com/login")
        line_bot_api.reply_message(replytoken, text_message)

    ## *** ถ้าเชื่อมโยงไปยัง database ได้จะทำการส่ง FAQ  *** ##
    elif text_re == "ex_answersheet":
        text_message = TextSendMessage("ลิงก์ตัวอย่างเเบบสอบถาม: https://cmblockage.cmfightflood.com/pdf/blockage_survey.pdf?fbclid=IwAR1dQ4ZWODhPhW7ItG7X3s8aQO8cIJHHDiLtoJSwMr_Cm5GwnB_yxwO0PJ8")
        line_bot_api.reply_message(replytoken, text_message)

    ## *** เเจ้งปัญหา *** ##
    elif text_re == "reportProblem":
        text_message = TextSendMessage("กรุณาส่งอำเภอเเละตำบลในรูปแบบ ตำบล/อำเภอ มาให้ทางเราคะ เช่น สุเทพ/เมืองเชียงใหม่ ")
        line_bot_api.reply_message(replytoken, text_message)

    ## *** ถ้าเชื่อมโยงไปยัง database ได้จะทำการส่ง PDF ของ พื้นที่รับน้ำ เเต่ละอำเภอมาให้ ตามที่ส่ง อำเภอหรือจังหวัดมา  *** ##
    elif text_re == "พื้นที่รับน้ำ":
        text_message = TextSendMessage("*** อยู่ระหว่างรอข้อมูลพื้นที่รับน้ำ ***")
        line_bot_api.reply_message(replytoken, text_message)

    elif text_re == "คู่มือแก้ปัญหาสิ่งกีดขวางลำน้ำ":
        text_message = TextSendMessage("*** อยู่ระหว่างรอข้อมูลคู่มือการเเก้ปัญหาค่ะ ***")
        line_bot_api.reply_message(replytoken, text_message)      

    elif text_re == 'active_chatbot':

        carousel_reply = FlexSendMessage(
            alt_text="Flex Message alt text", 
            contents = {
                "type": "carousel",
                "contents": 
                [
                    {
                        "type": "bubble",
                        "body": 
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": 
                            [
                                {
                                    "type": "text",
                                    "text": "หน้าตัดลำน้ำ",
                                    "weight": "bold",
                                    "size": "xl",
                                    "wrap": True,
                                    "contents": []
                                },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": 
                                [
                                    {
                                        "type": "text",
                                        "text": "_",
                                        "size": "xxs",
                                        "color": "#FFFFFFFF",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": 
                                [
                                    {
                                        "type": "text",
                                        "text": "การวัดระยะของหน้าตัดลำน้ำ",
                                        "weight": "bold",
                                        "size": "xs",
                                        "flex": 0,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": 
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": 
                        [
                            {
                                "type": "button",
                                "action": 
                                {
                                    "type": "uri",
                                    "label": "การวัดพื้นที่หน้าตัด",
                                    "uri": "https://cmblockage.cmfightflood.com/images/ref_advice/1_4_2.jpg"
                                },

                            },
                                {
                                "type": "button",
                                "action": 
                                    {
                                    "type": "uri",
                                    "label": "ลักษณะสิ่งกีดขวาง",
                                    "uri": "https://cmblockage.cmfightflood.com/images/ref_advice/1_4_1.jpg"
                                    }
                                },
                                {
                                    "type": "button",
                                    "action": 
                                    {
                                        "type": "uri",
                                        "label": "ประเภทของสิ่งกีดขวาง",
                                        "uri": "https://cmblockage.cmfightflood.com/images/ref_advice/1_4_3.jpg"
                                    }
                                }
                            ]
                        }
                    },
                {
                    "type": "bubble",
                    "body": 
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": 
                        [
                            {
                                "type": "text",
                                "text": "ข้อมูลอื่นๆ ที่เกี่ยวข้อง",
                                "weight": "bold",
                                "size": "xl",
                                "wrap": True,
                                "contents": []
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": 
                                [
                                    {
                                        "type": "text",
                                        "text": "_",
                                        "size": "xxs",
                                        "color": "#FFFFFFFF",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": 
                                [
                                    {
                                        "type": "text",
                                        "text": "ลักษณะอื่นๆ ",
                                        "weight": "bold",
                                        "size": "xs",
                                        "flex": 0,
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": 
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": 
                        [
                            {
                                "type": "button",
                                "action": 
                                {
                                    "type": "uri",
                                    "label": "การดาดผิวของลำน้ำ",
                                    "uri": "https://cmblockage.cmfightflood.com/images/ref_advice/1_6.png"
                                },
                            },
                                {
                                    "type": "button",
                                    "action": 
                                    {
                                        "type": "uri",
                                        "label": "ความชันช่วงเกิดปัญหา",
                                        "uri": "https://cmblockage.cmfightflood.com/images/ref_advice/1_7.jpg"
                                    }
                                },
                            {
                                "type": "button",
                                "action": 
                                {
                                    "type": "uri",
                                    "label": " ",
                                    "uri": "https://cmblockage.cmfightflood.com/images/ref_advice/1_4_3.jpg"
                                }
                            }
                        ]
                    }
                }
            ]
        })

        # text_message = TextSendMessage("ระบบถามตอบข้อสงสัยทั่วไป Chatbot.")
        line_bot_api.reply_message(replytoken, carousel_reply)

    elif text_re == "ข้อมูลสิ่งกีดขวาง":
        flexReply = FlexSendMessage(
            alt_text="Flex Message alt text", 
            contents =
                        {
                            "type": "bubble",
                            "direction": "ltr",
                            "body": 
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": 
                                [
                                    {
                                        "type": "button",
                                        "action": 
                                        {
                                            "type": "message",
                                            "label": "สิ่งกีดขวางใกล้ฉัน",
                                            "text": "สิ่งกีดขวางใกล้ฉัน"
                                        }
                                    },
                                    {
                                        "type": "button",
                                        "action":
                                        {
                                             "type": "message",
                                             "label": "สิ่งกีดขวางรายตำบล",
                                             "text": "สิ่งกีดขวางรายตำบล"
                                        }
                                    },
                                    {
                                        "type": "button",
                                        "action": 
                                        {
                                            "type": "message",
                                            "label": "สิ่งกีดขวางรายอำเภอ",
                                            "text": "สิ่งกีดขวางรายอำเภอ"
                                        }
                                    }
                                ]
                            }
                        })
        # location
        # เลือกสถานที่

        # text_message = TextSendMessage(text='โปรดส่ง {} ของคุณมาให้เราค่ะ'.format(text_re))
        line_bot_api.reply_message(replytoken, flexReply)

    elif text_re == "สิ่งกีดขวางใกล้ฉัน":
        text_message = TextSendMessage(text='โปรดส่งโลเคชั่นของคุณมาให้เราค่ะ')
        line_bot_api.reply_message(replytoken, text_message)

    elif text_re == "เลือกสถานที่":
        text_re = "กรุณาส่ง จังหวัด อำเภอ ตำบล ในรูปแบบ จังหวัด/อำเภอ/ตำบล"
        text_message = TextSendMessage(text='โปรดส่ง {} ของคุณมาให้เราค่ะ'.format(text_re))
        line_bot_api.reply_message(replytoken, text_message)

    elif text_re == "สิ่งกีดขวางรายตำบล":
        text_re = "ชื่ออำเภอเเละชื่อตำบล"
        text_message = TextSendMessage(text='โปรดส่ง {} ที่ท่านต้องการมาให้เราในรูปแบบ ตำบล/อำเภอ ตัวอย่างเช่น สุเทพ/เมืองเชียงใหม่'.format(text_re))
        line_bot_api.reply_message(replytoken, text_message)

    elif text_re == "สิ่งกีดขวางรายอำเภอ":
        text_re = "ชื่ออำเภอ"
        text_message = TextSendMessage(text='โปรดส่ง {} ที่ท่านต้องการมาให้เราค่ะ'.format(text_re))
        line_bot_api.reply_message(replytoken, text_message)
 
    # elif text_re == "Facebook":
    #     text_message = TextSendMessage('https://www.facebook.com/CENDiMcmu')
    #     line_bot_api.reply_message(replytoken, text_message)

    # elif text_re == "website":
    #     text_message = TextSendMessage('https://cendim.eng.cmu.ac.th/')
    #     line_bot_api.reply_message(replytoken, text_message)

    # elif text_re == "ที่อยู่":
    #     text_message = TextSendMessage("ติดต่อเรา\nคณะวิศวกรรมศาสตร์ มหาวิทยาลัยเชียงใหม่ 239 ถนนห้วยแก้ว ตำบลสุเทพ อำเภอเมือง จังหวัดเชียงใหม่ 50200\nโทร : 053942010 , 053944156\nEmail : cendim@eng.cmu.ac.th")
    #     line_bot_api.reply_message(replytoken, text_message)


def menu_card(replytoken):

    # Debug Menu card is response.
    # print("This function is menu card")

    ##### คำสั่งสร้าง Card #####
    # ## เพิ่ม card ตรงนี้

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
            
                ## 1) ข้อมูลสิ่งกีดขวางทางน้ำ ในจังหวัดเชียงใหม่ 
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/images/linebot/blockage_box1.png?fbclid=IwAR2YaG8CkW_OrBwgMNPE8KrxupZF5IMWxgNcZfog4GV4RneZdjgcYSzBdSY',
                    title='ข้อมูลสิ่งกีดขวางทางน้ำในจังหวัดเชียงใหม่',
                    text='โปรดเลือกหัวข้อดังนี้', 
                    actions=[
                        MessageAction(
                            label='ข้อมูลสิ่งกีดขวาง',  
                            text='ข้อมูลสิ่งกีดขวาง'  
                        ),
                        MessageAction(
                            label='เเจ้งปัญหา',
                            text='เเจ้งปัญหา'
                        ),
                        MessageAction(
                            label=' ',
                            text=' '
                        )

                    ]
                ),
                ### 2) สำรวจสิ่งกีดขวางทางน้ำเพิ่มเติม
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/images/linebot/blockage_box2.png?fbclid=IwAR2EIFMwuXKWyolCWRm1FUlSFx5zViH5Ci5ZG2cdk2V4u3nrU9AzFl28bt8',
                    title='สำรวจสิ่งกีดขวางทางน้ำเพิ่มเติม',
                    text='โปรดเลือกหัวข้อดังนี้',
                    actions=[
                         MessageAction(
                            label='เก็บข้อมูล',
                            text='กรอกข้อมูลเเบบสำรวจ'
                        ),
                        MessageAction(
                            label='ตัวอย่างเเบบสำรวจ',  
                            text='ตัวอย่างเเบบสำรวจ'  
                        ),
                        MessageAction(
                            label=' ',
                            text=' '
                        )
                    ]
                ),
                ### 3)  ข้อมูลสนับสนุน (IDF, รูปแบบสิ่งกีดขวาง Pattern ต่าง ๆ)
                CarouselColumn(
                    thumbnail_image_url='https://cmblockage.cmfightflood.com/images/linebot/blockage_box2.png?fbclid=IwAR2EIFMwuXKWyolCWRm1FUlSFx5zViH5Ci5ZG2cdk2V4u3nrU9AzFl28bt8',
                    title='สำรวจสิ่งกีดขวางทางน้ำเพิ่มเติม',
                    text='โปรดเลือกหัวข้อดังนี้',
                    actions=[
                         MessageAction(
                            label=' คู่มือแก้ปัญหาสิ่งกีดขวาง',
                            text='คู่มือแก้ปัญหาสิ่งกีดขวางลำน้ำ'
                        ),
                        MessageAction(
                            label='ข้อมูลพื้นที่รับน้ำ',  
                            text='พื้นที่รับน้ำ'  
                        ),
                        MessageAction(
                            label='รูปแบบสิ่งกีดขวาง',
                            text='ข้อสงสัยเเบบสำรวจ'
                        )
                    ]
                )

 
            ]
        )
    )


    #### จบ คำสั่งสร้าง Card ####
    ### คำสั่ง return Card ออกไปหา user ###
    line_bot_api.reply_message(replytoken, carousel_template_message)


#########################################################################
#########################################################################
#########################################################################
 


###########################
### Location API function #
###########################

def reply_location(latitude, longitude, replyToken, api_menu):

    ######################
    ## API Blockages ##
    ######################

    ## ข้อมูล blockage ที่ใกล้ที่สุด ## #############################################################################################################################  

    if api_menu == "ข้อมูลสิ่งกีดขวาง":
        longitude = float(longitude)
        latitude = float(latitude) 
        # print('location la long = ',longitude, latitude) 
        data = requests.get('https://cmblockage.cmfightflood.com/location_test2/{}/{}'.format(latitude, longitude))
        # print('Show data = ', data)
        json_data = json.loads(data.text)
        # print('json_data = ',json_data)
        num = len(json_data)

        # print("json data", json_data, '\n')
        message = "ลำดับที่ใกล้ที่สุดไปไกลที่สุด \n"
        text_message = TextSendMessage(text=message)

        # print('Check here')
        array = []
        # array_data = []
        # list_test = [] ## for test location 
        i = 0
        while i in range(num):
        
            location_message = LocationSendMessage(
                title= "{}".format(json_data[i]['location']),

                blk_code = json_data[i]['blk_code'],
                blk_id = json_data[i]['blk_id'],
                # title= "Location",
                address="{} {} {} {} {}".format(json_data[i]['latitude_start'], json_data[i]['longitude_start'],
                json_data[i]['blk_code'], json_data[i]['blk_id'], json_data[i]['thumbnail_name']),
                
                # พอดีเขียน สลับ la long
                latitude=json_data[i]['longitude_start'],
                longitude=json_data[i]['latitude_start']
            )
            # print(location_message)
            array.append(location_message)
            # print("array",i ,' ', array)
            i += 1


        json_loca = json.loads(str(array))
        # print('len: ', len(json_loca))
        # print('\n')
        # for i in json_loca:
        #     print('json_loca:', i)

        template_co = []

        for push_element in json_loca:
            split_data = push_element['address']
            array_data = split_data.split(' ')

            longitude = array_data[0]
            latitude = array_data[1]
            blk_code = array_data[2]
            blk_id = array_data[3]
            thumbnail_name = array_data[4]

            address = push_element['title']
            img_path = thumbnail_name
 
            flex_reply = FlexSendMessage(
                alt_text="Flex Message alt text", 
                contents= {
                            "type": "bubble",
                            "hero": 
                            {
                                "type": "image",
                                "url": "https://cmblockage.cmfightflood.com/{}".format(img_path), 
                            "size": "full", 
                            "aspectRatio": "20:13", 
                            "aspectMode": "cover",
                                "action": 
                                {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": "https://linecorp.com/"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": address,
                                        "weight": "bold",
                                        "size": "md",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": blk_code, 
                                                "size": "sm", 
                                                "color": "#999999", 
                                                "flex": 0, 
                                                "margin": "md", 
                                                "contents": []
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ตำเเหน่ง",
                                                    "uri": 'https://www.google.co.th/maps/place/{},{}'.format(latitude, longitude)
                                                }
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "รายละเอียด",
                                                    "uri": 'https://cmblockage.cmfightflood.com/report/pdf/{}'.format(blk_id)
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        })

            template_co.append(flex_reply)
        line_bot_api.reply_message(replyToken, template_co)
 

 

#########################################################################

def reply_text(menu_api, text, replytoken):

    if menu_api == 'testing':
        text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        line_bot_api.reply_message(replytoken, text_message)


    ######################
    # location_blk API
    ######################

    elif menu_api == "เลือกสถานที่":
        # print("เลือกสถานที่ active")
        arrayW = text.split('/')
        # print(arrayW)

        province = arrayW[0]
        ampol = arrayW[1]
        tumbol = arrayW[2]

 

        data = requests.get('https://cmblockage.cmfightflood.com/find_location_blk/{}/{}/{}'.format(province, ampol, tumbol))

        # print("Data show ::", data)
        # print("Content Show ::", data.content)

        json_data = json.loads(data.text)
        # print("json_data",json_data)

        # for i in json_data:
        #     print("เลือกสถานที่: ",i)
        
        template_co = []

     
        for element in json_data:
            # 0:blk_code 1:blk_id, 2:latitude_start, 3:longitude_start, 4:location
            array_dict = []
            
            for j in element:
                array_dict.append(element[j])
            
            # print("array_dict: ",array_dict)
 
            flex_reply = FlexSendMessage(
                    alt_text="Flex Message alt text", 
                    contents= 
                    {
                        "type": "bubble",
                        "hero":
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": 
                            [
                                {
                                    "type": "text",
                                    "text": array_dict[4],  ## เก็บ idCode:  address blk_code
                                    "weight": "bold",
                                    "size": "md",  
                                    "color": "#2e2e1f",
                                    "wrap": True,
                                    "contents": []
                                },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": 
                                [
                                    {
                                        "type": "text",
                                        "text": array_dict[0],  ## เก็บ Location: blk_code address
                                        "weight": "regular", 
                                        "size": "xs",
                                        "color": "#1FB802FF",
                                        "flex": 0,
                                        "align": "start",
                                        "gravity": "top",
                                        "margin": "none",
                                        "wrap": True,
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "separator"
                            }
                            ]
                        },
                        "footer": 
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": 
                            [
                                {
                                    "type": "button",
                                    "action": 
                                    {
                                        "type": "uri",
                                        "label": "ตำแหน่งที่ตั้ง",
                                        "uri": 'https://www.google.co.th/maps/place/{},{}'.format(array_dict[2], array_dict[3])
                            },
                        },
                        {
                            "type": "button",
                            "action": 
                            {
                                "type": "uri",
                                "label": "รายละเอียด",
                                "uri":  'https://cmblockage.cmfightflood.com/report/pdf/{}'.format(array_dict[1])
                            }
                        }
                    ]
                }
                })
            
            template_co.append(flex_reply)

        line_bot_api.reply_message(replytoken, template_co)
           
    elif menu_api == "สิ่งกีดขวางรายตำบล":

        # print("สิ่งกีดขวางรายตำบล active")
        arrayW = text.split('/')
        # print('arrayW: ',arrayW)

        tumbol = arrayW[0] 
        ampol = arrayW[1] 
        
        # data = requests.get('http://127.0.0.1:8000/find_location_blk_tumbol/{}/{}'.format(ampol, tumbol)) ## test
        data = requests.get('https://cmblockage.cmfightflood.com/find_location_blk_tumbol/{}/{}'.format(tumbol, ampol))
 
        json_data = json.loads(data.text)
        count_json_data = len(json_data)
        
        # print('สิ่งกีดขวางรายตำบล--->',count_json_data)

        if count_json_data > 0:
        # print('\n')

            arrayMax = []
            

            for element in json_data:
                # 0:blk_code 1:blk_id, 2:latitude_start, 3:longitude_start, 4:location
                array_dict = []
                for j in element:
                    array_dict.append(element[j])
                
                arrayMax.append(array_dict)
    
            template_co = []

            print('arrayMax',arrayMax)

            while True:
                if len(arrayMax) == 1:
                    print(1)
                    carousel_tp = CT.templateCount_1(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0]

                elif len(arrayMax) == 2:
                    print(2)
                    carousel_tp = CT.templateCount_2(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:2]

                elif len(arrayMax) == 3:
                    print(3)
                    carousel_tp = CT.templateCount_3(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:4]

                elif len(arrayMax) == 4:
                    print(4)
                    carousel_tp = CT.templateCount_4(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:5]

                elif len(arrayMax) == 5:
                    print(5)
                    carousel_tp = CT.templateCount_5(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:6]

                elif len(arrayMax) == 6:
                    print(6)
                    carousel_tp = CT.templateCount_6(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:7]

                elif len(arrayMax) == 7:
                    print(7)
                    carousel_tp = CT.templateCount_7(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:8]

                elif len(arrayMax) == 8:
                    print(8)
                    carousel_tp = CT.templateCount_8(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:9]

                elif len(arrayMax) == 9:
                    print(9)
                    carousel_tp = CT.templateCount_9(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:10]

                elif len(arrayMax) >= 10:
                    print(10)
                    carousel_tp = CT.templateCount_10(arrayMax)
                    template_co.append(carousel_tp)
                    del arrayMax[0:11]

                elif len(arrayMax) <= 0:
                    break
    

            # template_co.append(carousel_template_message)

            line_bot_api.reply_message(replytoken, template_co)
        else:
            msg_error = "ไม่พบอำเภอหรือตำบลนี้ในระบบคะ \n \nกรุณาตรวจสอบการสะกดคำให้ถูกต้อง หรือรูปแบบการส่งข้อมูลให้อยู่ในเเบบ 'ตำบล/อำเภอ' ด้วยค่ะ"
            error_reply = TextSendMessage(msg_error)
            line_bot_api.reply_message(replytoken, error_reply)


    elif menu_api == "สิ่งกีดขวางรายอำเภอ":

        ampol_active = ['ไชยปราการ','ดอยหล่อ','ดอยสะเก็ด','ฝาง','สะเมิง','สันกำแพง','สันทราย','สันป่าตอง','สารภี','หางดง','เมืองเชียงใหม่','แม่ริม','แม่วาง','แม่ออน','แม่อาย']

        if text in ampol_active:
            template_co = []
    
            link_pdf = "https://cmblockage.cmfightflood.com/reports/solution/pdf?amp={}&tumbol=sum".format(text)
            carousel_template_message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url="https://cmblockage.cmfightflood.com/images/pic_mapAmp/{}.PNG".format(text),
                            title= "ข้อมูลสิ่งกีดขวาง",
                            text=  text, 
                            actions=[
                                URIAction(
                                    label='ไฟล์ PDF', 
                                    uri= link_pdf
                                    )
                                ]
                            )
                        ]
                    )
                )
                
            template_co.append(carousel_template_message)
            line_bot_api.reply_message(replytoken, template_co)
        
        else:
            msg_error = "ไม่พบอำเภอนี้ในระบบคะ กรุณาลองตรวจสอบการสะกดคำ หรือเลือกอำเภอที่มีในระบบดังนี้คะ \n \n'ไชยปราการ',\n'ดอยหล่อ',\n'ดอยสะเก็ด',\n'ฝาง',\n'สะเมิง',\n'สันกำแพง',\n'สันทราย',\n'สันป่าตอง',\n'สารภี',\n'หางดง',\n'เมืองเชียงใหม่',\n'แม่ริม',\n'แม่วาง',\n'แม่ออน',\n'แม่อาย'"

            error_reply = TextSendMessage(msg_error)
            line_bot_api.reply_message(replytoken, error_reply)
            

  
    ######################
    # Mockup Solution ###
    ######################

    elif menu_api == "เเจ้งปัญหา":
        str = text.split('/')
        print('str-->',str)
        tumbol = str[0]  
        aumpol = str[1]  
        # print(aumpol, '\n')
        # print(tumbol, '\n')

        # data = requests.get('http://127.0.0.1:8000/problem_report/{}/{}'.format(aumpol,tumbol)) ## test 
        data = requests.get('https://cmblockage.cmfightflood.com/problem_report/{}/{}'.format(tumbol, aumpol))

        json_data = json.loads(data.text)
        num = len(json_data)
        print('เเจ้งปัญหา-->', num)

        # Check Json print logs
        # print("json data", json_data, '\n')
        # print("id_station: ", json_data[0]['id_station'])
        # print("tumbol: ", json_data[0]['tumbol'])
        # print("link_report: ", json_data[0]['link_report'])

        if num > 0:
            message = ""

            for i in range(num):
                id_station = json_data[i]['id_station']
                tumbol_hq = json_data[i]['tumbol']
                link_report = json_data[i]['link_report']
                tel = json_data[i]['tel']
                tumbol = tumbol_hq[3:]
                # tumbol_hq = '\033[1m'+' '+'\033[4m' + tumbol_hq + '\033[0m'

                mess = '{}. {} \n ตำบล: {} \n อำเภอ: {}  \n หมายเลขติดต่อ: {} \n ลิงก์ {}' .format(
                    i+1, tumbol_hq, tumbol, aumpol, tel, link_report)
                message = message + mess + "\n"

            # print(message)
            text_message = TextSendMessage(text=message)
            line_bot_api.reply_message(replytoken, text_message)

        else:
            msg_error = "ไม่พบอำเภอหรือตำบลนี้ในระบบคะ \n \nกรุณาตรวจสอบการสะกดคำให้ถูกต้อง หรือรูปแบบการส่งข้อมูลให้อยู่ในเเบบ 'ตำบล/อำเภอ' ด้วยค่ะ"
            error_reply = TextSendMessage(msg_error)
            line_bot_api.reply_message(replytoken, error_reply)


#########################################################################


if __name__ == "__main__":
    app.run()
