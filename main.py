import requests
import math
from art import text2art
from discord import message
from discord.ext import commands, tasks
from discord import client
from discord import Member
import discord
import re

key = "Your key here"

bot = commands.Bot(command_prefix='>')

@bot.command()
async def skills(ctx, vrpid):
    exp = 0
    char = 0
    player = requests.get(f'https://tycoon-w8r4q4.users.cfx.re/status/dataadv/{vrpid}',
        headers={
        "X-Tycoon-Key" : key
        })

    player = player.json()

    em = discord.Embed(title= f"{vrpid}'s Skills", color=discord.Color.red())
    # Get Hunting LVL
    exp = player['data'].get('gaptitudes_v').get('hunting').get('skill')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Hunting", value=f"Level {exp}", inline=True)

    # Get Biz LVL
    exp = player['data'].get('gaptitudes_v').get('business').get('business')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Business", value=f"Level {exp}", inline=True)

    # Get Strength
    exp = player['data'].get('gaptitudes_v').get('physical').get('strength')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Strength", value=f"Level {exp}", inline=True)

    # Get EMS
    exp = player['data'].get('gaptitudes_v').get('ems').get('ems')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="EMS", value=f"Level {exp}", inline=True)

    # Get Firefighter
    exp = player['data'].get('gaptitudes_v').get('ems').get('fire')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Fire Fighter", value=f"Level {exp}", inline=True)

    # Get post op
    exp = player['data'].get('gaptitudes_v').get('trucking').get('postop')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Post Op", value=f"Level {exp}", inline=True)

    # Get trucking
    exp = player['data'].get('gaptitudes_v').get('trucking').get('trucking')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Trucking", value=f"Level {exp}", inline=True)

    # Get garbage
    exp = player['data'].get('gaptitudes_v').get('trucking').get('garbage')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Garbage", value=f"Level {exp}", inline=True)

    # Get mechanic
    exp = player['data'].get('gaptitudes_v').get('trucking').get('mechanic')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Mechanic", value=f"Level {exp}", inline=True)

    # Get gambling
    exp = player['data'].get('gaptitudes_v').get('casino').get('casino')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Gambling", value=f"Level {exp}", inline=True)

    # get bus
    exp = player['data'].get('gaptitudes_v').get('train').get('bus')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Bus Driver", value=f"Level {exp}", inline=True)

    # Get train
    exp = player['data'].get('gaptitudes_v').get('train').get('train')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Conductor", value=f"Level {exp}", inline=True)

    # Get player
    exp = player['data'].get('gaptitudes_v').get('player').get('player')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Player", value=f"Level {exp}", inline=True)

    # Get racing
    exp = player['data'].get('gaptitudes_v').get('player').get('racing')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Racing", value=f"Level {exp}", inline=True)

    # Get farming
    exp = player['data'].get('gaptitudes_v').get('farming').get('farming')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Farming", value=f"Level {exp}", inline=True)

    # Get fishing
    exp = player['data'].get('gaptitudes_v').get('farming').get('fishing')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Fishing", value=f"Level {exp}", inline=True)

    # Get mining
    exp = player['data'].get('gaptitudes_v').get('farming').get('mining')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Mining", value=f"Level {exp}", inline=True)

    # Get flying commercial
    exp = player['data'].get('gaptitudes_v').get('piloting').get('piloting')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Airline Pilot", value=f"Level {exp}", inline=True)

    # Get flying cargo
    exp = player['data'].get('gaptitudes_v').get('piloting').get('cargos')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Cargo Pilot", value=f"Level {exp}", inline=True)

    # Get heli
    exp = player['data'].get('gaptitudes_v').get('piloting').get('heli')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="Heli Pilot", value=f"Level {exp}", inline=True)

    exp = player['data'].get('gaptitudes_v').get('piloting').get('heli')
    exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
    em.add_field(name="** **", value="** **", inline=True)

    await ctx.send(embed = em)

@bot.command()
async def company(ctx, vrpid):
    compname = "No company found"
    rank = "No company rank found"
    voucherData = "No voucher data located"
    manager = False
    player = requests.get(f'https://tycoon-w8r4q4.users.cfx.re/status/dataadv/{vrpid}',
        headers={
        "X-Tycoon-Key" : key
        })

    player = player.json()
    em = discord.Embed(title= f"{vrpid}'s Company Info", color=discord.Color.red())

    company = player['data'].get('groups')

    company = str(company)

    if "corp9" in company:
        compname = "Rockwell Corporation: Rockwell Transport Solutions"
        if "tier1" in company:
            rank = "Initiate"
        if "tier2" in company:
            rank = "Lead Foot"
        if "tier3" in company:
            rank = "Wheelman"
        if "tier4" in company:
            rank = "Legenday Wheelman"
        if "tier5" in company:
            rank = "Speed Demon"
        if "manager" in company:
            manager = True

        try:
            vouch = player['data'].get('inventory').get('rts_voucher_air').get('amount')
        except:
            vouch = 0
        try:
            vouch1 = player['data'].get('inventory').get('rts_voucher_heavy').get('amount')
        except:
            vouch1 = 0
        try:
            vouch2 = player['data'].get('inventory').get('rts_voucher').get('amount')
        except:
            vouch2 = 0

        totalV = int(vouch) + int(vouch1) + int(vouch2)

        voucherData = f'\nRegular vouchers: {vouch2}\nAviator Vouchers: {vouch}\nHeavy Vouchers: {vouch1}\n\nTotal Vouchers: {totalV}'

    if "corp11" in company:
        compname = "Rockwell Corporation: Panda's Illicit Gains Syndicate"

        try:
            stolen = player['data'].get('inventory').get('stolen_money').get('amount')
        except:
            stolen = 0

        try:
            voucher = player['data'].get('inventory').get('pigs_voucher').get('amount')
        except:
            voucher = 0

        voucherData = f"\nStolen Money: {stolen}\nVouchers: {voucher}"

        if "tier1" in company:
            rank = "Hustler"
        if "tier2" in company:
            rank = "Pickpocket"
        if "tier3" in company:
            rank = "Thief"
        if "tier4" in company:
            rank = "Lawless"
        if "tier5" in company:
            rank = "Criminal Mastermind"
        if "tier6" in company:
            rank = "Overlord"
        if "manager" in company:
            manager = True

    if "corp2" in company:
        print(player['data'].get('inventory'))
        compname = "CollinsCo"

        if "tier1" in company:
            rank = "Rookie Carrier"
        if "tier2" in company:
            rank = "Cheap Fare"
        if "tier3" in company:
            rank = "Transporter"
        if "tier4" in company:
            rank = "Navigator"
        if "tier5" in company:
            rank = "Transit Specialist"
        if "tier6" in company:
            rank = "No Lifer"
        if "manager" in company:
            manager = True

        try:
            fVoucher = player['data'].get('inventory').get('stolen_money').get('amount')
        except:
            stolen = 0

        try:
            cVoucher = player['data'].get('inventory').get('pigs_voucher').get('amount')
        except:
            voucher = 0
        try:
            tVoucher = player['data'].get('inventory').get('pigs_voucher').get('amount')
        except:
            voucher = 0
        try:
            sVoucher = player['data'].get('inventory').get('pigs_voucher').get('amount')
        except:
            voucher = 0

        voucherData = f"\nCabbie Vouchers: {stolen}\nFlyie Vouchers: {voucher}"


    em.add_field(name="Company", value=compname, inline=False)
    em.add_field(name="Company Rank", value=rank, inline=False)
    if manager == True:
        em.add_field(name="Other", value="Manager", inline=False)
    em.add_field(name="Voucher Data", value=voucherData, inline=False)

    await ctx.send(embed = em)

bizList = ['biz_wenger', 'biz_vacaloco', 'biz_vespucci_masks', 'biz_liquor_ss', 'biz_cablecar', 'biz_spoke_bikes', 'biz_integrity', 'biz_hookies', 'biz_horny_burgie', 'biz_caseys_diner', 'biz_youtool_ss', 'biz_granny', 'biz_korean_plaza', 'biz_baracuda', 'biz_lcport_house', 'biz_yellowjack', 'biz_elboo', 'biz_bishops_chicken', 'biz_docks_ls', 'biz_gas_harmony', 'biz_jetsam_ls', 'biz_jetsam_pb', 'biz_catfish', 'biz_banner', 'biz_uginc_gs', 'biz_persons', 'biz_sisyphus', 'biz_lcstau_house', 'biz_alphamail_lsia', 'biz_hospital_parking_strawberry', 'biz_venetian', 'biz_mazebank_arena', 'biz_stay_frosty', 'biz_rebel', 'biz_cluckingbell_co', 'biz_millars', 'biz_lcstau_casino', 'biz_opium_hotel', 'biz_merryweather', 'biz_quarry', 'biz_pbcc', 'biz_lcssv_house', 'biz_tung', 'biz_stripclub', 'biz_bahama_mamas', 'biz_kortz', 'biz_zancudo', 'biz_lcport_mansion', 'biz_ltweld', 'biz_airfield_ss', 'biz_racetrack_vw', 'biz_carrier', 'biz_fyrecay', 'biz_train_paleto', 'biz_train_grapeseed', 'biz_train_davis', 'biz_train_docks', 'biz_train_terminal', 'biz_train_sandy', 'biz_train_lm', 'biz_train_mp', 'biz_train_lc', 'biz_shipyard_pa', 'biz_pier_400', 'biz_raven', 'biz_walker', 'biz_lsia', 'biz_murrietta_oil', 'biz_oilrig', 'biz_lcssv_aeroport', 'biz_chiliad_base', 'biz_lcssv_dam', 'biz_windfarm', 'biz_dp_pier', 'biz_pacific_standard', 'biz_playboi', 'biz_vineyard', 'biz_satn']

bizName = ['Wenger Institute', 'La Vaca Loco', 'Vespucci Movie Masks', 'Sandy Shores Liquor', 'Sandy Shores Aerial Tramway', 'Mr Spoke Bike rental', '4 Integrity Way', 'Hookies', "Horny's Burgers", "Casey's Diner", 'You Tool Sandy Shores', "Grandma's House", 'Korean Plaza', 'Barracuda Cafe', 'Portland Safehouse', 'Yellowjack', 'Lârss & Elboö', "Bishop's Chicken", 'Los Santos Docks', 'Harmony Gas Station', 'Jetsam Terminal', 'Jetsam Paleto Bay', 'Catfish View', 'Banner Hotel and Spa', 'Union Grain Inc Grapeseed', 'Parsons Rehabilitation Center', 'Sisyphus Theater', 'Staunton Island Safehouse', 'Alphamail Couriers LSIA', 'Medical Center Parking Garage', 'Venetian', 'Mazebank Arena', 'Fridgit Co.', 'Rebel Radio', 'Clucking bell Co', "Millars Boat Shop", 'Staunton Island Casino', 'Opium Nights Hotel', "Bristol's Storage", 'Davis Quartz Quarry', 'Pacific Bluffs Country Club', 'Shoreside Vale Safehouse', 'Jonny Tung', 'Vanilla Unicorn', 'Bahama Mamas', 'KO RTZ', 'Fort Zancudo', 'Portland Mansion', 'LT Weld', 'Sandy Shores Airfield', 'Vinewood RaceTrack', 'Aircraft Carrier', 'Train Yard: Cayo Perico', 'Train Yard: Paleto Bay', 'Train Yard: Grapeseed', 'Train Yard: Davis Quartz', 'Train Yard: Los Santos Docks', 'Train Yard: Terminal', 'Train Yard: Sandy Shores', 'Train Yard: La Mesa', 'Train Yard: Mirror Park', 'Ship Yard: Portland', 'Pacific Allied Shipyard', 'Pier 400', 'Raven Slaughterhouse', 'Walker Logistics', 'Los Santos International Airport', 'Collins Petrochemical Corp', 'Oil Platform', 'Francis International Airport', 'Mt Chiliad Base', 'Cochrane Dam', 'Ron Alternates Wind Farm', 'Del Perro Pier', 'Pacific Standard Bank', 'Playboy Mansion', 'Tongva Hills Vineyard', 'San Andreas Telecom Network']

bizCost = [15000, 150000, 150000, 250000, 250000, 250000, 300000, 300000, 300000, 350000, 500000, 500000, 750000, 750000, 750000, 950000, 1500000, 1500000, 1500000, 2500000, 3000000, 3500000, 4000000, 4000000, 4500000, 4500000, 5000000, 5000000, 6000000, 7500000, 8000000, 8000000, 9000000, 11000000, 12500000, 15000000, 17000000, 17500000, 18000000, 18000000, 20000000, 25000000, 30000000, 32000000, 35000000, 35000000, 35000000, 37000000, 47000000, 60000000, 65000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 8000000, 120000000, 125000000, 125000000, 125000000, 150000000, 200000000, 250000000, 350000000, 350000000, 500000000, 550000000, 600000000, 750000000]

bizBonus = [2590, 13604, 13604, 19990, 19990, 19990, 22963, 22963, 22963, 25831, 33967, 33974, 46515, 46515, 46515, 55935, 80078, 80078, 80078, 120056, 138848, 157069, 174818, 174818, 192169, 192169, 209176, 209176, 242317, 242317, 290267, 305862, 305862, 336557, 396262, 439813, 510497, 565612, 579217, 592757, 592757, 646313, 776557, 902575, 952001, 1025219, 1025219, 1025219, 1073468, 1308944, 1603569, 1714115, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2861836, 2961540, 2961540, 2961540, 3451593, 4397437, 5308689, 7057315, 7057315, 0, 10359526, 11155977, 13493131]

bizRun = 0

@bot.command()
async def biz(ctx, vrpid):
    bizToMax = 0
    bizToMax2 = 0
    bizDaily = 0
    bizDailyTax = 0
    nextBiz = ""
    tyStorage = 0
    ltWeld = 0
    bizSpent = 0
    bizRun = 0
    biz = requests.get(f'https://tycoon-w8r4q4.users.cfx.re/status/getuserbiz/{vrpid}',
        headers={
        "X-Tycoon-Key" : key
        })

    biz = biz.json()

    em = discord.Embed(title= f"{vrpid}'s Business Info", color=discord.Color.red())

    for i in range(0,78):
        lvl = (biz['businesses'].get(bizList[bizRun]))
        print(f"{bizName[bizRun]}: Level {lvl}")
        if lvl == None:
            lvl = 0
            if nextBiz == "" or nextBiz == "N/A":
                nextBiz = bizName[bizRun]
            bizToMax = bizToMax + bizCost[bizRun]
        bizSpent = lvl*bizCost[bizRun] + bizSpent
        bizToMax2 = (100-lvl)*bizCost[bizRun] + bizToMax2

        if lvl == 0:
            bizDaily = bizDaily + 0
        elif lvl > 0:
            bizDaily = (bizBonus[bizRun] + (bizBonus[bizRun]*(lvl-1)*0.25)) + bizDaily

        if lvl > 0 and bizRun > 51 and bizRun < 62:
            tyStorage = tyStorage + (1840*lvl)

        if lvl > 0 and bizRun == 48:
            ltWeld = lvl*57500

        if nextBiz == "":
            nextBiz = "N/A"
        elif nextBiz == "N/A" and lvl < 100 and bizList[bizRun] != "biz_pacific_standard":
            nextBiz = bizName[bizRun]

        bizRun += 1

    if "biz_pacific_standard" in str(biz):
        bizDailyTax = math.trunc(bizDaily * 0.8)
    else:
        bizDailyTax = math.trunc(bizDaily * 0.7)

    bizToMax2 -= 49500000000

    em.add_field(name="Total spent on businesses", value=f"${format(bizSpent, ',')}", inline=False)
    em.add_field(name="Money until all businesses are owned", value=f"${format(bizToMax, ',')}", inline=False)
    em.add_field(name="Money until all businesses are maxed", value=f"${format(bizToMax2, ',')}", inline=False)
    em.add_field(name="Business daily before tax", value=f"${format(bizDaily, ',')}", inline=False)
    em.add_field(name="Business Daily after tax", value=f"${format(bizDailyTax, ',')}", inline=False)
    em.add_field(name="Next recommended business to purchase", value=nextBiz, inline=False)
    em.add_field(name="Trainyard Storage", value=f"{format(tyStorage, ',')} Kg", inline=False)
    em.add_field(name="LT Weld Storage", value=f"{format(ltWeld, ',')} Kg", inline=False)

    await ctx.send(embed = em)

@bot.command()
async def id(ctx, snowflake):
    dsid = requests.get(f'https://tycoon-w8r4q4.users.cfx.re/status/snowflake2user/{snowflake}',
        headers={
        "X-Tycoon-Key" : key
        })

    dsid = dsid.json()
    dsid = dsid.get("user_id")
    if dsid == None:
        dsid = "N/A"
    await ctx.send(f"The ID requested is **{dsid}**")

@bot.command()
async def inv(ctx, vrpid):
    invRun = 0
    invL = ''
    inv = requests.get(f'https://tycoon-w8r4q4.users.cfx.re/status/dataadv/{vrpid}',
        headers={
        "X-Tycoon-Key" : key
        })

    inv = inv.json()
    inv = inv['data'].get('inventory')

    print(inv)
    await ctx.send(f"The inventory of {vrpid} has been sent to you via DMs!")
    try:
        await ctx.author.send(inv)
    except:
        await ctx.author.send("The requested inventory was too large to send! This will be fixed eventually.")

@bot.command()
async def bal(ctx, server, vrpid):
    serverL = ['OS', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'SA']
    serverN = ['https://tycoon-w8r4q4.users.cfx.re/', 'https://tycoon-2epova.users.cfx.re/', 'https://tycoon-2epovd.users.cfx.re/', 'https://tycoon-wdrypd.users.cfx.re/', 'https://tycoon-njyvop.users.cfx.re/', 'https://tycoon-2r4588.users.cfx.re/', 'https://tycoon-npl5oy.users.cfx.re/', 'https://tycoon-2vzlde.users.cfx.re/', 'https://tycoon-wmapod.users.cfx.re/', 'N/A']
    ip = ''
    balRun = 0
    while balRun < 10:
        if server.upper() == serverL[balRun]:
            ip = serverN[balRun]
            balRun = 10

            wealth = requests.get(f'{ip}status/wealth/{vrpid}',
                headers={
                "X-Tycoon-Key" : key
                })

            wealth = wealth.json()

            bank = wealth.get('bank')
            wallet = wealth.get('wallet')

            if bank == None and wallet == None:
                await ctx.send("Please make sure you used the correct player ID, this player does not appear to be online!")
            elif bank == 0 and wallet == 0:
                await ctx.send("Please make sure you used the correct player ID, this player appears to be broke!")
            else:
                em = discord.Embed(title= f"{vrpid}'s Wealth", color=discord.Color.red())

                em.add_field(name="Wallet", value=f"${format(wallet, ',')}", inline=False)
                em.add_field(name="Bank", value=f"${format(bank, ',')}", inline=False)
                em.add_field(name="Total", value=f"${format(bank+wallet, ',')}", inline=False)

                await ctx.send(embed = em)

        elif balRun == 9:
            await ctx.send("The requested server cannot be found, please try again")
            balRun = 100
        else:
            balRun += 1


@bot.command()
async def commands(ctx):
    em = discord.Embed(title= "Commands", color=discord.Color.red())

    em.add_field(name="id", value="Usage: >id [discordID] | Example: >id 238771447290527745", inline=False)
    em.add_field(name="skills", value="Usage: >skills [ingameID] | Example: >skills 256531", inline=False)
    em.add_field(name="biz", value="Usage: >biz [ingameID] | Example: >biz 256531", inline=False)
    em.add_field(name="company", value="Usage: >company [ingameID] | Example: >company 256531", inline=False)
    em.add_field(name="bal", value="Usage: >bal [server] [ingameID] | Example: >bal OS 256531 | Requires player to be online!", inline=False)

    await ctx.send(embed = em)


print("Bot Online")
bot.run('Discord bot token here')
