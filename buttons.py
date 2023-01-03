from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup

til=ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("🇺🇿 Uzbek",),
		],

	],
	resize_keyboard=True
)

shaxarlar=ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("Mirobod"),
			KeyboardButton("Uchtepa"),
			KeyboardButton("Olmazor"),
			KeyboardButton("Bektemir"),
			KeyboardButton("Yunusobod")
		],
		[
			KeyboardButton("Mirzo-Ulug'bek🤴")

		],
		[
			KeyboardButton("Sergili"),
			KeyboardButton("Shayxontoxur",),
			KeyboardButton("Yashnabod"),
			KeyboardButton("Chilonzor"),
			KeyboardButton("Yakkasaroy")

		],



	],
	resize_keyboard=True
)


tel_raqam=ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("Raqamingizni yozing📞:",request_contact=True),
			KeyboardButton("Lakatsiya📍:",request_location=True),
		]	
	],
	resize_keyboard=True
)



buyurtma_qilish=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Buyurtma qilish ☺️",callback_data="zakaz"),
		],
	

	]
)

b_menu=ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("Mening manzilm⛳️"),
			KeyboardButton("Buyurtmalar🔔"),
			KeyboardButton("Ariza va Shikoyatlar⛔️"),
		],
		[
			KeyboardButton("MENU✅"),
			KeyboardButton("MANDS tog'risida malumot♥️"),
			KeyboardButton("Sozlamalar⚒")

		],

	],
	resize_keyboard=True
)






menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Barcha menyular",callback_data="barcha"),	
			InlineKeyboardButton("Settings ⚙️",callback_data="set"),
		],
		[
			InlineKeyboardButton("Boshqa🍟🍕",callback_data="boshqa"),
			InlineKeyboardButton("Lavash 🌯",callback_data="lavash"),
		],
		[
				
			InlineKeyboardButton("Hot-dog 🌭",callback_data="hot-dog"),
			InlineKeyboardButton("Haggi🌮",callback_data="haggi"),
		],
		[
			
			InlineKeyboardButton("Toster🍗",callback_data="toster"),	
			InlineKeyboardButton("Gamburger🍔",callback_data="gamburger"),
			
		],
		[
			InlineKeyboardButton("Clap-sendvich 🍗",callback_data="clap"),
			InlineKeyboardButton("Shirinliklar🍰🧁🎂",callback_data="shirin"),

		],
		[
			InlineKeyboardButton("Ichimliklar🍸🥃🍷",callback_data="ichimlik"),
		],


	],




)

lavash_menu =InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Tovuqli lavash 🌯",callback_data="tovuq lavash"),	
			InlineKeyboardButton("Go'shtli lavash 🌯",callback_data="goshtli lavash"),
			
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back1"),
		],


	],
)

ll_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Mini lavash🌯🍗",callback_data="mini"),
			InlineKeyboardButton("Sirli lavash🌯🍗🧀",callback_data="sirli")

		],
		[
			InlineKeyboardButton("Qalampirli lavash🌯🍗🌶",callback_data="qalampr"),
			InlineKeyboardButton("Oddiy lavash🌯🍗",callback_data="odiy"),
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back2"),
		],

	],

)

gg_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Mini lavash🌯🥩",callback_data="min"),
			InlineKeyboardButton("Sirli lavash🌯🧀🥩",callback_data="sirl")

		],
		[
			InlineKeyboardButton("Qalampirli lavash🌯🌶🥩",callback_data="qalamp"),
			InlineKeyboardButton("Oddiy lavash🌯🥩",callback_data="odi"),
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back4"),
		],

	],

)








kk_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back3"),
		],



	]
)






hotdog_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Korolevski 🌭",callback_data="korol"),
			InlineKeyboardButton("Oddiy 🌭",callback_data="oddiy"),
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back5"),
		],

	],
)

kkk_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back6"),
		],



	]
)





haggi_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Haggi tovuqli🌮",callback_data="tovu"),
			InlineKeyboardButton("Haggi Go'shtli🌮",callback_data="gosh"),
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back7"),
		],

	]
)

hag_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back8"),
		],



	]
)








toster_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Chicken 🥪🍗",callback_data="tovu1"),
			InlineKeyboardButton("Go'shtli 🥪🥩 ",callback_data="gosh2"),
			
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back9"),
		],

	],
)

tos_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back10"),
		],



	]
)





gam_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Bigburger 🍔",callback_data="big"),
			InlineKeyboardButton("Gamburger 🍔",callback_data="odiy1"),
			InlineKeyboardButton("Bigcheese 🍔",callback_data="sir1"),


		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back11"),
		],

	],
)

gam_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back12"),
		],



	]
)



clap_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Clap-Chicken 🥪🍗",callback_data="layle"),
			InlineKeyboardButton("Clap-Meat 🥪🥩",callback_data="meat"),


		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back13"),	
		],

	],
)

clap_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back14"),
		],



	]
)






suv_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Sharbat 🧃",callback_data="blis"),
			InlineKeyboardButton("Gazli ichimliklar 🥃",callback_data="cola"),
			InlineKeyboardButton("Kofe ☕️",callback_data="kofe"),
			
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back15"),	
		]

	]
)
gaz_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Coca-cola⚫️",callback_data="coc"),
			InlineKeyboardButton("Fanta🟠",callback_data="fanta"),
		],
			
		[	
			InlineKeyboardButton("Sprite🟢",callback_data="sprite"),
			InlineKeyboardButton("Pepsi⚫️",callback_data="pepsi"),


		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back18"),
		],


	],
)

gaz_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back19"),
		],



	]
)



blis_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("olma🍏",callback_data="oo"),
			InlineKeyboardButton("o'rik🍑",callback_data="or"),

		],
		[
			InlineKeyboardButton("anor🧃",callback_data="ano"),
			InlineKeyboardButton("olcha🍒",callback_data="ol"),

		],
		[
			InlineKeyboardButton("qulupnay🍓",callback_data="qul"),
			InlineKeyboardButton("Banan🍌",callback_data="ban"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back177"),
		],

	],
)


suv_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back16"),
		],



	]
)


kf_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Qora kofe ☕️",callback_data="qor"),
			InlineKeyboardButton("Kapuchino ☕️",callback_data="kop"),
		],

		[	
			InlineKeyboardButton("ortga🔙",callback_data="back20"),


		],

	],
)

kf_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back21"),
		],



	]
)


shrn_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Praga 🥮",callback_data="praga"),
			InlineKeyboardButton("Ptichi-moloko 🧁",callback_data="qush"),
			InlineKeyboardButton("Chees-cake 🍰",callback_data="cak"),
			
		],

		[
			InlineKeyboardButton("ortga🔙",callback_data="back22"),
		],

	],
)
pp_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back23"),
		],



	]
)






bshq_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Kartoshka-fri 🍟",callback_data="kar"),
			InlineKeyboardButton("Derevenskoe 🍟",callback_data="dala"),
			InlineKeyboardButton("Pizza 🍕",callback_data="piz"),
			
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back24"),
		],

	],
)

pizza_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("pizza sirli 🍕",callback_data="pzs"),
			InlineKeyboardButton("Pizza Korona 🍕",callback_data="koro"),
			InlineKeyboardButton("Pizza Oddiy 🍕",callback_data="pizod"),
			
		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back25"),
		],

	],
)


pzza_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back26"),
		],



	]
)



kdp_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="back25"),
		],



	]
)
st_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Mavjud emas ❌🚫",callback_data="ex"),
			InlineKeyboardButton("ortga🔙",callback_data="orqaga"),


		],

	]
)


k_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("1️⃣",callback_data="bir"),
			InlineKeyboardButton("2️⃣",callback_data="ikki"),
			InlineKeyboardButton("3️⃣",callback_data="uch"),
		],
		[
			InlineKeyboardButton("4️⃣",callback_data="tor"),
			InlineKeyboardButton("5️⃣",callback_data="besh"),
			InlineKeyboardButton("6️⃣",callback_data="olti"),
		],
		[
			InlineKeyboardButton("7️⃣",callback_data="yetti"),
			InlineKeyboardButton("8️⃣",callback_data="sakkiz"),
			InlineKeyboardButton("9️⃣",callback_data="toqqiz"),

		],
		[
			InlineKeyboardButton("ortga🔙",callback_data="orqaga"),
		],



	]
)


qwerty_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("ortga🔙",callback_data="back32"),	
		],

	],
)
