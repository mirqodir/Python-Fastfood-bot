import logging
from config import *
from aiogram import Bot, Dispatcher, executor, types
from buttons import * 
from aiogram.types import Message,CallbackQuery


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Tilni tanlang / choose language",reply_markup=til)
    print(message.from_user.username)


#bu til tanlanganda uzga kradi
@dp.message_handler(text="🇺🇿 Uzbek")
async def til_tanlash(message:types.Message):
    await message.answer("Tumaningizni tanlang:",reply_markup=shaxarlar )






    

#shaxar tnlaganda usha shaxarga kradi
@dp.message_handler(text="Mirzo-Ulug'bek🤴")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )



@dp.message_handler(text="Mirobod")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )


@dp.message_handler(text="Uchtepa")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )


@dp.message_handler(text="Olmazor")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )


@dp.message_handler(text="Bektemir")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )


@dp.message_handler(text="Yunusobod")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )


@dp.message_handler(text="Sergili")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating :",reply_markup=tel_raqam )


@dp.message_handler(text="Shayxontoxur")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )

@dp.message_handler(text="Yashnabod")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )


@dp.message_handler(text="Chilonzor")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )

@dp.message_handler(text="Yakkasaroy")
async def til_tanlash(message:types.Message):
    await message.answer("Telefon nomeringizni va Qayerga yetkazb berish kerakligini jonating:",reply_markup=tel_raqam )



#jonaatiladigan nomerri ushab qoladi
@dp.message_handler(content_types=["contact",])
async def til_tanlash(message):
    await message.answer("Buyurtma qilmoqchi bo'lgan raqamingiz qabul qlindi:",reply_markup=buyurtma_qilish)




@dp.callback_query_handler(text="zakaz")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )
    await call.message.answer("menu",reply_markup=b_menu )


@dp.message_handler(text="Manzil o'zgartirish⛳️")
async def til_tanlash(message:types.Message):
    await message.answer("O'zgartirmoqchi bo'lgan manzilingizni kiriting:",reply_markup=b_menu )


@dp.message_handler(text="Buyurtmalar🔔")
async def til_tanlash(message:types.Message):
    await message.answer("Buyurtmani amalga oshiring:",reply_markup=b_menu )

@dp.message_handler(text="Ariza va Shikoyatlar⛔️")
async def til_tanlash(message:types.Message):
    await message.answer("Arizangizni yozing:",reply_markup=b_menu )

@dp.message_handler(text="MENU✅")
async def til_tanlash(message:types.Message):
    await message.answer("menu:",reply_markup=b_menu )

@dp.message_handler(text="MANDS tog'risida malumot♥️")
async def til_tanlash(message:types.Message):
    await message.answer("MANDS brendi dunyodagi eng oldi brendlaridan🏆🥇:",reply_markup=b_menu )

@dp.message_handler(text="Sozlamalar⚒")
async def til_tanlash(message:types.Message):
    await message.answer("ok:",reply_markup=b_menu )







###############################################################################################################lambaw

#lavash knopkasini chqazadi
@dp.callback_query_handler(text="lavash")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=lavash_menu )

@dp.callback_query_handler(text="tovuq lavash")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("tanlang",reply_markup=ll_menu )



@dp.callback_query_handler(text="goshtli lavash")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("tanlang",reply_markup=gg_menu )

@dp.callback_query_handler(text="mini")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/lavashmini.jpg","rb"),
        caption="""Narxi:   18 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)

   


@dp.callback_query_handler(text="sirli")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/sirlilavash.jpg","rb"),
        caption="""Narxi:   24 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips, pomidor,pishloq, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)


@dp.callback_query_handler(text="qalampr")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/accq.jpg","rb"),
        caption="""Narxi:   28 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips,qalampr, pomidor,pishloq, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)



@dp.callback_query_handler(text="odiy")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/od.jpg","rb"),
        caption="""Narxi:   28 000 so'm
Tarkibi: Xamir, tovuq go`sht, chips,qalampr, pomidor,pishloq, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)



@dp.callback_query_handler(text="min")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/od.jpg","rb"),
        caption="""Narxi:   28 000 so'm
Tarkibi: Xamir, mol go`sht, chips,qalampr, pomidor,pishloq, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)


@dp.callback_query_handler(text="sirl")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/od.jpg","rb"),
        caption="""Narxi:   28 000 so'm
Tarkibi: Xamir, mol go`sht, chips,pishloq, pomidor,pishloq, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)


@dp.callback_query_handler(text="qalamp")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/od.jpg","rb"),
        caption="""Narxi:   28 000 so'm
Tarkibi: Xamir, mol go`sht, chips,qalampr, pomidor,pishloq, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)

@dp.callback_query_handler(text="odi")
async def til_tanlash(call:CallbackQuery):
    # await call.message.answer("tanlang",reply_markup=kk_nopka )
    await call.message.answer_photo(
        photo=open("images/od.jpg","rb"),
        caption="""Narxi:   28 000 so'm
Tarkibi: Xamir, mol go`sht, chips,qalampr, pomidor,pishloq, bodring, sous, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=kk_nopka)

  

####################################################################################################ortga_f
################lavash_back
@dp.callback_query_handler(text="back1")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )


@dp.callback_query_handler(text="back2")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=lavash_menu )

@dp.callback_query_handler(text="back3")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=ll_menu )

@dp.callback_query_handler(text="back4")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=gg_menu )

#################################################################################hot_dog_menuuu
@dp.callback_query_handler(text="hot-dog")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=hotdog_menu )

@dp.callback_query_handler(text="korol")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/karol.jpg","rb"),
        caption="""Narxi:  23 000 so'm
Tarkibi: Kunjutli bulochka, Sosiska, Tuzlangan bodring, Pomidor, Ketchup, Mayonez, 
Miqdorini tanlang yoki kiriting""",reply_markup=kkk_nopka)

@dp.callback_query_handler(text="oddiy")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/oddiy.jpg","rb"),
        caption="""Narxi:  16 000 so'm
Tarkibi: Kunjutli bulochka, Sosiska, Tuzlangan bodring, Pomidor, Ketchup, Mayonez, 
Miqdorini tanlang yoki kiriting""",reply_markup=kkk_nopka)

    

#######################################################################################hotdog back
@dp.callback_query_handler(text="back5")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )


@dp.callback_query_handler(text="back6")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=hotdog_menu )

################################################################################################
#######################################################################################  Haggi_buttons
@dp.callback_query_handler(text="haggi")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=haggi_menu )

@dp.callback_query_handler(text="tovu")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/xtovu.jpg","rb"),
        caption="""Narxi: 28 000 so'm
Tarkibi:Bulochka,tovuq go'shti,pishloq,salat bargi,sous,Pamidor,Bodiring,Mayanez,
Miqdorini tanlang yoki kiriting""",reply_markup=hag_nopka)

@dp.callback_query_handler(text="gosh")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/xgosh.jpg","rb"),
        caption="""Narxi: 28 000 so'm
Tarkibi:Bulochka,mol go'shti,pishloq,salat bargi,sous,Pamidor,Bodiring,Mayanez,
Miqdorini tanlang yoki kiriting""",reply_markup=hag_nopka)
   



###############################################################################################haggi back##
@dp.callback_query_handler(text="back8")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=haggi_menu )

@dp.callback_query_handler(text="back7")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )


######################################################################################## toster_buttons
@dp.callback_query_handler(text="toster")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=toster_menu )

@dp.callback_query_handler(text="tovu1")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/ttovu.jpg","rb"),
        caption="""Narxi: 28 000 so'm
Tarkibi:Toster noni,Mayanez,Ketchup,Tovuq goshti ,pomidor,Bodiring,salat bargi,Pishloq
Miqdorini tanlang yoki kiriting""",reply_markup=tos_nopka)

@dp.callback_query_handler(text="gosh2")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tgosh.jpg","rb"),
        caption="""Narxi: 28 000 so'm
Tarkibi:Toster noni,Mayanez,Ketchup,Mol goshti ,pomidor,Bodiring,salat bargi,Pishloq
Miqdorini tanlang yoki kiriting""",reply_markup=tos_nopka)
######################################################################################################### toster back
@dp.callback_query_handler(text="back9")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )

@dp.callback_query_handler(text="back10")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=toster_menu )





############################################################################################### gamburger_buttons
@dp.callback_query_handler(text="gamburger")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=gam_menu )

@dp.callback_query_handler(text="big")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/bburger.jpg","rb"),
        caption="""Narxi: 28 000 so'm
Tarkibi:Bulochka,Kotlet Mol Go'shti,Bodiring,Pomidor,Salat bargi,Ketchup Mayanez
Miqdorni kiriting yoki tanlang""",reply_markup=gam_nopka)

@dp.callback_query_handler(text="sir1")
async def til_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open("images/sburger.jpg","rb"),
        caption="""Narxi: 33 000 so'm
Tarkibi:Bulochka,Kotlet Mol Go'shti,Bodiring,Pomidor,Salat bargi,Pishloq,Ketchup ,Mayanez
Miqdorni kiriting yoki tanlang""",reply_markup=gam_nopka)
    

@dp.callback_query_handler(text="odiy1")
async def til_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open("images/burg.jpg","rb"),
        caption="""Narxi: 22 000 so'm
Tarkibi:Bulochka,Kotlet Mol Go'shti,Bodiring,Pomidor,Salat bargi,Ketchup Mayanez
Miqdorni kiriting yoki tanlang""",reply_markup=gam_nopka)
############################################################################################################### gam_back
@dp.callback_query_handler(text="back11")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )

@dp.callback_query_handler(text="back12")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=gam_menu )



############################################################################################# clap_sendvich
@dp.callback_query_handler(text="clap")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=clap_menu )

@dp.callback_query_handler(text="layle")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/ctovu.jpg","rb"),
        caption="""Narxi: 28 000 so'm
Tarkibi:Toster noni,Tovuq Go'shti,Bodiring,Pomidor,Salat bargi,Ketchup Mayanez
Miqdorni kiriting yoki tanlang""",reply_markup=clap_nopka)

@dp.callback_query_handler(text="meat")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cc.jpg","rb"),
        caption="""Narxi: 28 000 so'm
Tarkibi:Toster noni, Mol Go'shti,Bodiring,Pomidor,Salat bargi,Ketchup Mayanez
Miqdorni kiriting yoki tanlang""",reply_markup=clap_nopka)
###################################################################################################clap_back
@dp.callback_query_handler(text="back13")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )

@dp.callback_query_handler(text="back14")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=clap_menu )





#######################################################################################icimliklar_
@dp.callback_query_handler(text="ichimlik")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=suv_menu )
########################################################################################cola menu
@dp.callback_query_handler(text="cola")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=gaz_menu)



@dp.callback_query_handler(text="coc")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cococo.jpg","rb"),
        caption="""Narxi: 10 000 so'm
Tarkibi: Gazli ichimlik
Miqdorini tanlang yoki kiriting""",reply_markup=gaz_nopka)


@dp.callback_query_handler(text="fanta")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/fanta.jpg","rb"),
        caption="""Narxi: 10 000 so'm
Tarkibi: Gazli ichimlik
Miqdorini tanlang yoki kiriting""",reply_markup=gaz_nopka)

@dp.callback_query_handler(text="sprite")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/sprite.jpg","rb"),
        caption="""Narxi: 11 000 so'm
Tarkibi: Gazli ichimlik
Miqdorini tanlang yoki kiriting""",reply_markup=gaz_nopka)

@dp.callback_query_handler(text="pepsi")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/pepsi.jpg","rb"),
        caption="""Narxi: 10 000 so'm
Tarkibi: Gazli ichimlik
Miqdorini tanlang yoki kiriting""",reply_markup=gaz_nopka)

##################################################################################################blis menu
@dp.callback_query_handler(text="blis")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("Sharbatlar",reply_markup=blis_menu )

@dp.callback_query_handler(text="oo")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/olma.jpg","rb"),
        caption="""Narxi: 12 000 so'm
Tarkibi: Olma Sharbati
Miqdorini tanlang yoki kiriting""",reply_markup=suv_nopka)

@dp.callback_query_handler(text="or")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/orik.jpg","rb"),
        caption="""Narxi: 12 000 so'm
Tarkibi: O'rik Sharbati
Miqdorini tanlang yoki kiriting""",reply_markup=suv_nopka)

@dp.callback_query_handler(text="ano")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/anor1.jpg","rb"),
        caption="""Narxi: 12 000 so'm
Tarkibi: Anor Sharbati
Miqdorini tanlang yoki kiriting""",reply_markup=suv_nopka)

@dp.callback_query_handler(text="ol")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/olcha.jpg","rb"),
        caption="""Narxi: 12 000 so'm
Tarkibi: Olcha Sharbati
Miqdorini tanlang yoki kiriting""",reply_markup=suv_nopka)


@dp.callback_query_handler(text="qul")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/qulupnay.jpg","rb"),
        caption="""Narxi: 12 000 so'm
Tarkibi: Qulupnay Sharbati
Miqdorini tanlang yoki kiriting""",reply_markup=suv_nopka)

@dp.callback_query_handler(text="ban")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/bababa.jpg","rb"),
        caption="""Narxi: 12 000 so'm
Tarkibi: Banan Sharbati
Miqdorini tanlang yoki kiriting""",reply_markup=suv_nopka)


@dp.callback_query_handler(text="kofe")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("Kofe",reply_markup=kf_menu )


@dp.callback_query_handler(text="qor")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/qq.jpg","rb"),
        caption="""Narxi: 15 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=kf_nopka)


@dp.callback_query_handler(text="kop")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/66332.jpg","rb"),
        caption="""Narxi: 15 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=kf_nopka)



###################################################################################################suv_back


@dp.callback_query_handler(text="back15")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )

@dp.callback_query_handler(text="back16")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=blis_menu )

@dp.callback_query_handler(text="back177")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=suv_menu )

@dp.callback_query_handler(text="back18")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=suv_menu )

@dp.callback_query_handler(text="back19")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=gaz_menu )

@dp.callback_query_handler(text="back20")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=suv_menu )

@dp.callback_query_handler(text="back21")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=kf_menu )






##############################################################################################wirinliklar
@dp.callback_query_handler(text="shirin")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=shrn_menu )



@dp.callback_query_handler(text="cak")
async def til_tanlash(call:CallbackQuery):
        await call.message.answer_photo(
        photo=open("images/777.jpg","rb"),
        caption="""Narxi: 42 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=pp_nopka)


@dp.callback_query_handler(text="praga")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/123.jpg","rb"),
        caption="""Narxi: 23 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=pp_nopka)

@dp.callback_query_handler(text="qush")
async def til_tanlash(call:CallbackQuery):
        await call.message.answer_photo(
        photo=open("images/1263.jpg","rb"),
        caption="""Narxi: 31 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=pp_nopka)
    


@dp.callback_query_handler(text="orqaga")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )
###############################################################################################################shrn_menu back
@dp.callback_query_handler(text="back22")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )

@dp.callback_query_handler(text="back23")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=shrn_menu )





###########################################################################################################boshqa____

@dp.callback_query_handler(text="boshqa")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=bshq_menu )

@dp.callback_query_handler(text="dala")
async def til_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open("images/556.jpg","rb"),
        caption="""Narxi: 15 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=kdp_nopka)


@dp.callback_query_handler(text="piz")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=pizza_menu )

@dp.callback_query_handler(text="pzs")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/555.jpg","rb"),
        caption="""Narxi: 45 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=pzza_nopka)



@dp.callback_query_handler(text="koro")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/87930581.jpg","rb"),
        caption="""Narxi: 48 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=pzza_nopka)

@dp.callback_query_handler(text="pizod")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/987.jpg","rb"),
        caption="""Narxi: 50 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=pzza_nopka)
    




@dp.callback_query_handler(text="kar")
async def til_tanlash(call:CallbackQuery):
     await call.message.answer_photo(
        photo=open("images/39.jpg","rb"),
        caption="""Narxi: 9 000 so'm
Miqdorini tanlang yoki kiriting""",reply_markup=kdp_nopka)
    


#orqaga chqazadigan knopka
@dp.callback_query_handler(text="back24")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )

@dp.callback_query_handler(text="back25")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=bshq_menu )

@dp.callback_query_handler(text="back26")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=pizza_menu )



##############################################################################################settingiz
@dp.callback_query_handler(text="set")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=st_menu )

@dp.callback_query_handler(text="ex")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("❌❌❌❌",reply_markup=st_menu )

@dp.callback_query_handler(text="orqaga")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer("quyidagilardan birini tanlang",reply_markup=menu )

@dp.callback_query_handler(text="bir")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )

@dp.callback_query_handler(text="ikki")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )

@dp.callback_query_handler(text="uch")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )

@dp.callback_query_handler(text="tor")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )

@dp.callback_query_handler(text="besh")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )

@dp.callback_query_handler(text="olti")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )


@dp.callback_query_handler(text="yetti")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )


@dp.callback_query_handler(text="sakkiz")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )


@dp.callback_query_handler(text="toqqiz")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi❤️",show_alert=True )



# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)