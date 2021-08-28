################################
# Transport tycoon API bot     #
# Made by Rhys                 #
# Last updated 17/08/2021      #
################################

import requests
import math
import discord
from discord.ext import commands
import asyncio
import time
from datetime import datetime
from discord.ext import tasks
import pymongo
from pymongo import MongoClient

if True == True:
    bot = commands.Bot(command_prefix='>')
    key = "your key here"
    token = 'your bot token here'
    defaultServer = "https://tycoon-2epova.users.cfx.re/"
    try:
        onlineS = requests.get("https://tycoon-w8r4q4.users.cfx.re/status/widget/players.json", timeout=10)
        onlineS = onlineS.json()
        defaultServer = "https://tycoon-w8r4q4.users.cfx.re/"
    except:
        try:
            onlineS = requests.get("https://tycoon-2epova.users.cfx.re/status/widget/players.json", timeout=10)
            onlineS = onlineS.json()
            defaultServer = "https://tycoon-2epova.users.cfx.re/"
        except:
            onlineS = requests.get("https://tycoon-2epovd.users.cfx.re/status/widget/players.json", timeout=10)
            onlineS = onlineS.json()
            defaultServer = "https://tycoon-2epovd.users.cfx.re/"


    print(f"The default server is: {defaultServer}")
    '''
    Skills
    '''
    @bot.command()
    async def skills(ctx, vrpid):
        cmdtime1 = time.perf_counter()
        exp = 0
        char = 0
        try:
            player = requests.get(f'{defaultServer}status/dataadv/{vrpid}',
                headers={
                "X-Tycoon-Key" : key
                }, timeout=10)

            player = player.json()

            skillRun = 0

            em = discord.Embed(title= f"{vrpid}'s Skills", color=discord.Color.red())

            skill1 = ['hunting', 'business', 'physical', 'ems', 'ems', 'trucking', 'trucking', 'trucking', 'trucking', 'casino', 'train', 'train', 'player', 'player', 'farming', 'farming', 'farming', 'piloting', 'piloting', 'piloting']
            skill2 = ['skill', 'business', 'strength', 'ems', 'fire', 'postop', 'trucking', 'garbage', 'mechanic', 'casino', 'bus', 'train', 'player', 'racing', 'farming', 'fishing', 'mining', 'piloting', 'cargos', 'heli']
            skill3 = ['Hunting', 'Business', 'Strength', 'EMS', 'Fire Fighter', 'Post Op', 'Trucking', 'Garbage', 'Mechanic', 'Gambling', 'Bus Driver', 'Conductor', 'Player', 'Racing', 'Farming', 'Fishing', 'Mining', 'Airline Pilot', 'Cargo Pilot', 'Heli Pilot']

            for i in range(0,19):
                exp = player['data'].get('gaptitudes_v').get(skill1[skillRun]).get(skill2[skillRun])
                exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
                em.add_field(name=skill3[skillRun], value=f"Level {exp}", inline=True)
                skillRun += 1

            exp = player['data'].get('gaptitudes_v').get('piloting').get('heli')
            exp = math.trunc((math.sqrt(1 + 8 * exp / 5) - 1) / 2)
            em.add_field(name="** **", value="** **", inline=True)

            await ctx.send(embed = em)

            cmdtime2 = time.perf_counter()
            cmdtime = (cmdtime2-cmdtime1)
            if debugging == True:
                await ctx.send(f"\nThe requested command took {cmdtime*1000}ms to complete")
        except:
            await ctx.send(f"User **{vrpid}**'s Skill data cannot be accessed, this could be due to a number of reasons")

    @bot.command()
    async def company(ctx, vrpid):
        cmdtime1 = time.perf_counter()
        compname = "No company found"
        rank = "No company rank found"
        voucherData = "No voucher data located"
        manager = False
        player = requests.get(f'{defaultServer}status/dataadv/{vrpid}',
            headers={
            "X-Tycoon-Key" : key
            }, timeout=10)

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
                fVoucher = player['data'].get('inventory').get('collinsco_cab_voucher').get('amount')
            except:
                fVoucher = 0

            try:
                cVoucher = player['data'].get('inventory').get('collinsco_plane_voucher').get('amount')
            except:
                cVoucher = 0
            try:
                tVoucher = player['data'].get('inventory').get('collinsco_train_voucher').get('amount')
            except:
                tVoucher = 0
            try:
                sVoucher = player['data'].get('inventory').get('collinsco_boat_voucher').get('amount')
            except:
                sVoucher = 0

            voucherData = f"\nCabbie Vouchers: {cVoucher}\nFlyie Vouchers: {fVoucher}\nTrainy Vouchers: {tVoucher}\nSeaman Vouchers: {sVoucher}\n\nTotal Vouchers: {sVoucher+tVoucher+fVoucher+cVoucher}"


        em.add_field(name="Company", value=compname, inline=False)
        em.add_field(name="Company Rank", value=rank, inline=False)
        if manager == True:
            em.add_field(name="Other", value="Manager", inline=False)
        em.add_field(name="Voucher Data", value=voucherData, inline=False)

        await ctx.send(embed = em)

        cmdtime2 = time.perf_counter()
        cmdtime = (cmdtime2-cmdtime1)
        if debugging == True:
            await ctx.send(f"\nThe requested command took {cmdtime*1000}ms to complete")

    bizList = ['biz_wenger', 'biz_vacaloco', 'biz_vespucci_masks', 'biz_liquor_ss', 'biz_cablecar', 'biz_spoke_bikes', 'biz_integrity', 'biz_hookies', 'biz_horny_burgie', 'biz_caseys_diner', 'biz_youtool_ss', 'biz_granny', 'biz_korean_plaza', 'biz_baracuda', 'biz_lcport_house', 'biz_yellowjack', 'biz_elboo', 'biz_bishops_chicken', 'biz_docks_ls', 'biz_gas_harmony', 'biz_jetsam_ls', 'biz_jetsam_pb', 'biz_catfish', 'biz_banner', 'biz_uginc_gs', 'biz_persons', 'biz_sisyphus', 'biz_lcstau_house', 'biz_alphamail_lsia', 'biz_hospital_parking_strawberry', 'biz_venetian', 'biz_mazebank_arena', 'biz_stay_frosty', 'biz_rebel', 'biz_cluckingbell_co', 'biz_millars', 'biz_lcstau_casino', 'biz_opium_hotel', 'biz_merryweather', 'biz_quarry', 'biz_pbcc', 'biz_lcssv_house', 'biz_tung', 'biz_stripclub', 'biz_bahama_mamas', 'biz_kortz', 'biz_zancudo', 'biz_lcport_mansion', 'biz_ltweld', 'biz_airfield_ss', 'biz_racetrack_vw', 'biz_carrier', 'biz_fyrecay', 'biz_train_paleto', 'biz_train_grapeseed', 'biz_train_davis', 'biz_train_docks', 'biz_train_terminal', 'biz_train_sandy', 'biz_train_lm', 'biz_train_mp', 'biz_train_lc', 'biz_shipyard_pa', 'biz_pier_400', 'biz_raven', 'biz_walker', 'biz_lsia', 'biz_murrietta_oil', 'biz_oilrig', 'biz_lcssv_aeroport', 'biz_chiliad_base', 'biz_lcssv_dam', 'biz_windfarm', 'biz_dp_pier', 'biz_pacific_standard', 'biz_playboi', 'biz_vineyard', 'biz_satn']

    bizName = ['Wenger Institute', 'La Vaca Loco', 'Vespucci Movie Masks', 'Sandy Shores Liquor', 'Sandy Shores Aerial Tramway', 'Mr Spoke Bike rental', '4 Integrity Way', 'Hookies', "Horny's Burgers", "Casey's Diner", 'You Tool Sandy Shores', "Grandma's House", 'Korean Plaza', 'Barracuda Cafe', 'Portland Safehouse', 'Yellowjack', 'Lârss & Elboö', "Bishop's Chicken", 'Los Santos Docks', 'Harmony Gas Station', 'Jetsam Terminal', 'Jetsam Paleto Bay', 'Catfish View', 'Banner Hotel and Spa', 'Union Grain Inc Grapeseed', 'Parsons Rehabilitation Center', 'Sisyphus Theater', 'Staunton Island Safehouse', 'Alphamail Couriers LSIA', 'Medical Center Parking Garage', 'Venetian', 'Mazebank Arena', 'Fridgit Co.', 'Rebel Radio', 'Clucking bell Co', "Millars Boat Shop", 'Staunton Island Casino', 'Opium Nights Hotel', "Bristol's Storage", 'Davis Quartz Quarry', 'Pacific Bluffs Country Club', 'Shoreside Vale Safehouse', 'Jonny Tung', 'Vanilla Unicorn', 'Bahama Mamas', 'KO RTZ', 'Fort Zancudo', 'Portland Mansion', 'LT Weld', 'Sandy Shores Airfield', 'Vinewood RaceTrack', 'Aircraft Carrier', 'Train Yard: Cayo Perico', 'Train Yard: Paleto Bay', 'Train Yard: Grapeseed', 'Train Yard: Davis Quartz', 'Train Yard: Los Santos Docks', 'Train Yard: Terminal', 'Train Yard: Sandy Shores', 'Train Yard: La Mesa', 'Train Yard: Mirror Park', 'Ship Yard: Portland', 'Pacific Allied Shipyard', 'Pier 400', 'Raven Slaughterhouse', 'Walker Logistics', 'Los Santos International Airport', 'Collins Petrochemical Corp', 'Oil Platform', 'Francis International Airport', 'Mt Chiliad Base', 'Cochrane Dam', 'Ron Alternates Wind Farm', 'Del Perro Pier', 'Pacific Standard Bank', 'Playboy Mansion', 'Tongva Hills Vineyard', 'San Andreas Telecom Network']

    bizCost = [15000, 150000, 150000, 250000, 250000, 250000, 300000, 300000, 300000, 350000, 500000, 500000, 750000, 750000, 750000, 950000, 1500000, 1500000, 1500000, 2500000, 3000000, 3500000, 4000000, 4000000, 4500000, 4500000, 5000000, 5000000, 6000000, 7500000, 8000000, 8000000, 9000000, 11000000, 12500000, 15000000, 17000000, 17500000, 18000000, 18000000, 20000000, 25000000, 30000000, 32000000, 35000000, 35000000, 35000000, 37000000, 47000000, 60000000, 65000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 80000000, 8000000, 120000000, 125000000, 125000000, 125000000, 150000000, 200000000, 250000000, 350000000, 350000000, 500000000, 550000000, 600000000, 750000000]

    bizBonus = [2590, 13604, 13604, 19990, 19990, 19990, 22963, 22963, 22963, 25831, 33974, 33974, 46515, 46515, 46515, 55935, 80078, 80078, 80078, 120056, 138848, 157069, 174818, 174818, 192169, 192169, 209176, 209176, 242317, 242317, 290267, 305862, 305862, 336557, 396262, 439813, 510497, 565612, 579217, 592757, 592757, 646313, 776557, 902575, 952001, 1025219, 1025219, 1025219, 1073468, 1308944, 1603569, 1714115, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2038284, 2861836, 2961540, 2961540, 2961540, 3451593, 4397437, 5308689, 7057315, 7057315, 0, 10359526, 11155977, 13493131]

    # bizBonus = [2590, 13604, 13604, 19990, 19990, 19990, 22963, 22963, 22963, 25831, 33974, 33974, 46515, 46515, 46515, 55935, 80078, 80078, 80078]

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
        nextBiz2 = ''
        bizRun = 0
        try:
            cmdtime1 = time.perf_counter()
            biz = requests.get(f'{defaultServer}status/getuserbiz/{vrpid}',
                headers={
                "X-Tycoon-Key" : key
                }, timeout=10)

            biz = biz.json()

            em = discord.Embed(title= f"{vrpid}'s Business Info", color=discord.Color.red())

            for i in range(0,78):
                upgraded = 0
                lvl = (biz['businesses'].get(bizList[bizRun]))
                if lvl == None:
                    lvl = 0
                    if nextBiz == "":
                        nextBiz = bizName[bizRun]
                    bizToMax = bizToMax + bizCost[bizRun]
                bizSpent = lvl*bizCost[bizRun] + bizSpent
                bizToMax2 = (100-lvl)*bizCost[bizRun] + bizToMax2

                if lvl != 100 and bizList[bizRun] != "biz_pacific_standard" and nextBiz2 == '':
                    nextBiz2 = bizName[bizRun]

                if nextBiz == "":
                    bizBuy = nextBiz2
                elif nextBiz != "":
                    bizBuy = nextBiz

                if lvl == 0:
                    bizDaily = bizDaily + 0
                elif lvl > 0:
                    bizDaily = math.trunc((bizBonus[bizRun] + (bizBonus[bizRun]*(lvl-1)*0.25)) + bizDaily)

                if lvl > 0 and bizRun > 51 and bizRun < 62:
                    tyStorage = tyStorage + (1840*lvl)

                if lvl > 0 and bizRun == 48:
                    ltWeld = lvl*57500

                bizRun += 1

            if "biz_pacific_standard" in str(biz):
                bizDailyTax = math.trunc(bizDaily * 0.8)
            else:
                bizDailyTax = math.trunc(bizDaily * 0.7)

            bizToMax2 -= 49500000000
            bizDaily = bizDaily - (bizDaily*0.01)
            bizDailyTax = bizDailyTax - (bizDailyTax*0.01)

            if bizBuy == "":
                bizBuy = "N/A"

            em.add_field(name="Total spent on businesses", value=f"${format(bizSpent, ',')}", inline=False)
            em.add_field(name="Money until all businesses are owned", value=f"${format(bizToMax, ',')}", inline=False)
            em.add_field(name="Money until all businesses are maxed", value=f"${format(bizToMax2, ',')}", inline=False)
            em.add_field(name="Business daily before tax", value=f"${format(bizDaily, ',')}", inline=False)
            em.add_field(name="Business Daily after tax", value=f"${format(bizDailyTax, ',')}", inline=False)
            em.add_field(name="Next recommended business to purchase", value=bizBuy, inline=False)
            em.add_field(name="Trainyard Storage", value=f"{format(tyStorage, ',')} Kg", inline=False)
            em.add_field(name="LT Weld Storage", value=f"{format(ltWeld, ',')} Kg", inline=False)
            em.set_footer(text = "Calculations assume you are in a faction with 1% tax, all values taken from rockwell website so if something isn't correct it is probably not my fault")

            cmdtime2 = time.perf_counter()
            cmdtime = (cmdtime2-cmdtime1)
            if debugging == True:
                await ctx.send(f"\nThe requested command took {cmdtime*1000}ms to complete")

            await ctx.send(embed = em)
        except Exception as e:
            await ctx.send(f"User **{vrpid}**'s Business information cannot be accessed, {e}")


    @bot.command()
    async def bizlist(ctx, vrpid):
        global bizRun
        biztxt = ''
        bizRun = 0
        biz = requests.get(f'{defaultServer}status/getuserbiz/{vrpid}',
            headers={
            "X-Tycoon-Key" : key
            }, timeout=10)

        biz = biz.json()

        for i in range(0,78):
            lvl = (biz['businesses'].get(bizList[bizRun]))
            if lvl == None:
                lvl = 0
            biztxt = f"{biztxt}\n{bizName[bizRun]}: Level {lvl}"
            bizRun += 1

        with open ('bizout.txt', 'wb') as bizout:
            bizout.write(biztxt.encode("utf-8"))
        await ctx.send(f"A list of **{vrpid}**'s businesses has been sent below")
        await ctx.send(file=discord.File('bizout.txt'))

    @bot.command()
    async def id(ctx, snowflake):
        dsid = requests.get(f'{defaultServer}status/snowflake2user/{snowflake}',
            headers={
            "X-Tycoon-Key" : key
            }, timeout=10)

        dsid = dsid.json()
        dsid = dsid.get("user_id")
        if dsid == None:
            dsid = "unable to be found"
        await ctx.send(f"The ID requested is **{dsid}**")


    remove2 = ['</span>', '<span style="color:orange">', '<span style="color:tomato">', "<span type='train-train'/>", '<span style="color:limegreen">', "<span type='piloting-piloting'/>", "<span class='rainbow'>", "<span type='casino-casino'/>", "<span type='trucking-garbage'/>", "<span type='trucking-garbage'/>", "<span type='physical-strength'/>", "<span type='piloting-cargos'/>", "<span type='ems-fire'/>", "<span type='trucking-postop'/>", "<span type='piloting-heli'/>", "<span style='color:purple'/>", '<span style="color:gold">', "<span type='player-player'/>", "<span type='business-business'/>", "<span type='trucking-trucking'/>", "<span/>", "<span style='color:crimson' n='14333'>", "<span>", "<span type='business-business'/>", "&#37"]


    @bot.command()
    async def inv(ctx, vrpid):
        cmdtime1 = time.perf_counter()
        dsid = requests.get(f'{defaultServer}status/dataadv/{vrpid}',
            headers={
            "X-Tycoon-Key" : "fz461IgfiQjE1BpHcxFqyPZajvDF6pq3mDnw0"
            }, timeout=10)

        dsid = dsid.json()
        dsid = dsid['data'].get('inventory')

        namelst = []
        quantitylst = []

        for key in dsid.keys():
            subdict = dsid[key]
            namelst.append(subdict["name"])
            quantitylst.append(subdict["amount"])

        invstr = ''
        invtxt = ''
        runi = 0
        for i in range(len(namelst)):

            invtxt = f"{namelst[runi]}: {quantitylst[runi]}\n" + invtxt
            invstr = f"<p>{namelst[runi]}: {quantitylst[runi]}</p>" + invstr
            runi += 1
        reprun = 0
        for i in range(len(remove2)):
            invtxt = invtxt.replace(remove2[reprun], '')
            reprun += 1
        invstr = f"<h1><p>{vrpid}'s inventory </p></h1><h3>{invstr}</h3>"
        with open ('out.txt', 'wb') as out:
            out.write(invtxt.encode("utf-8"))
        await ctx.send(f"The inventory of {vrpid} has been sent below")
        await ctx.send(file=discord.File('out.txt'))
        cmdtime2 = time.perf_counter()
        cmdtime = (cmdtime2-cmdtime1)
        if debugging == True:
            await ctx.send(f"\nThe requested command took {cmdtime*1000}ms to complete")
        '''
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_string(invstr, "out.pdf", configuration=config)
        '''


    @bot.command()
    async def invsearch(ctx, vrpid, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None):
        try:
            cmdtime1 = time.perf_counter()
            arglist = [arg1, arg2, arg3, arg4, arg5, arg6, arg7]
            argrun = 0
            args = ""
            for a in arglist:
                if arglist[argrun] != None:
                    argc = arglist[argrun].upper()
                    args = args + argc + " "
                argrun += 1
            args = args.rstrip(args[-1])
            if len(args) < 3:
                await ctx.send(f"A minimum of 3 characters is required, you specified {len(args)}")
            else:
                await ctx.send(f"Looking for **{args}** in **{vrpid}**'s inventory")

                dsid = requests.get(f'{defaultServer}status/dataadv/{vrpid}',
                    headers={
                    "X-Tycoon-Key" : "fz461IgfiQjE1BpHcxFqyPZajvDF6pq3mDnw0"
                    }, timeout=10)

                dsid = dsid.json()
                dsid = dsid['data'].get('inventory')

                namelst = []
                quantitylst = []

                for key in dsid.keys():
                    subdict = dsid[key]
                    namelst.append(subdict["name"])
                    quantitylst.append(subdict["amount"])
                namerun = 0
                item = False
                for p in (namelst):
                    if args in namelst[namerun].upper():
                        reprun = 0
                        item = namelst[namerun]
                        for i in remove2:
                            item = item.replace(remove2[reprun], '')
                            reprun += 1
                            print(reprun)
                        await ctx.send(f"**{vrpid}** has **{quantitylst[namerun]}** {item}")
                        item = True
                    namerun += 1
                if item == False:
                    await ctx.send(f"No **{args}** were found in **{vrpid}**'s inventory")
                cmdtime2 = time.perf_counter()
                cmdtime = (cmdtime2-cmdtime1)
                if debugging == True:
                    await ctx.send(f"\nThe requested command took {cmdtime*1000}ms to complete")
        except Exception as e:
            await ctx.send(f"An exception has occured: {e}")


    @bot.command()
    async def invpdf(ctx, vrpid):
        await ctx.send(f"The inventory of {vrpid} has been sent to you via DMs")
        await ctx.author.send("Coming soon")

    serverL = ['OS', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'SA']
    serverN = ['https://tycoon-w8r4q4.users.cfx.re/', 'https://tycoon-2epova.users.cfx.re/', 'https://tycoon-2epovd.users.cfx.re/', 'https://tycoon-wdrypd.users.cfx.re/', 'https://tycoon-njyvop.users.cfx.re/', 'https://tycoon-2r4588.users.cfx.re/', 'https://tycoon-npl5oy.users.cfx.re/', 'https://tycoon-2vzlde.users.cfx.re/', 'https://tycoon-wmapod.users.cfx.re/', 'N/A']
    ip = ''

    @bot.command()
    async def bal(ctx, server, vrpid):
        try:
            balRun = 0
            while balRun < 10:
                if server.capitalize() == serverL[balRun]:
                    ip = serverN[balRun]
                    balRun = 10

                    wealth = requests.get(f'{ip}status/wealth/{vrpid}',
                        headers={
                        "X-Tycoon-Key" : key
                        }, timeout=10)

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
        except Exception as e:
            await ctx.send(f"An exception has occured: {e}")

    @bot.command()
    async def commands(ctx):
        em = discord.Embed(title= "Commands", color=discord.Color.red())

        em.add_field(name="Id", value="Usage: >id [discordID] | Example: >id 238771447290527745 | Converts discord ID to ingame ID for use in other commands", inline=False)
        em.add_field(name="Skills", value="Usage: >skills [ingameID] | Example: >skills 256531 | Gets the player's skills", inline=False)
        em.add_field(name="Biz", value="Usage: >biz [ingameID] | Example: >biz 256531 | Gets the player's business stats", inline=False)
        em.add_field(name="Company", value="Usage: >company [ingameID] | Example: >company 256531 | Gets information about the player's company including vouchers", inline=False)
        em.add_field(name="Bal", value="Usage: >bal [server] [ingameID] | Example: >bal OS 256531 | Gets the player's ingame balance, requires player to be online!", inline=False)
        em.add_field(name="Github", value="Usage: >github | Example: >github | Gets the github link for the bot (may not be fully updated)", inline=False)
        em.add_field(name="Dxp", value="Usage: >dxp | Example: >dxp | Gives or removes the DXP Pings role from you", inline=False)
        em.add_field(name="Online", value="Usage: >online [ingameID] | Example: >online 256531 | Checks whether a user is online", inline=False)
        em.add_field(name="Inv", value="Usage: >inv [ingameID] | Example: >inv 256531 | Gives you a .txt file of a user's inv", inline=False)
        em.add_field(name="Invsearch", value="Usage: >invsearch [ingameID] [item]| Example: >invsearch 256531 exp | Finds the items a user has in their inventory and backpack", inline=False)
        em.add_field(name="Bizlist", value="Usage: >bizlist [ingameID] | Example: >bizlist 256531 | Gets a list of a users business levels", inline=False)

        await ctx.send(embed = em)

    @bot.command()
    async def github(ctx):
        await ctx.send("https://github.com/Alpacaception/tt-api-bot")


    @bot.command()
    async def dxp(ctx):
        user = ctx.message.author
        role = discord.utils.get(user.guild.roles, name="DXP Pings")
        if role in user.roles: #checks all roles the member has
            await user.remove_roles(role) #removes the role
            await ctx.send(f"Removed the DXP Pings role from **{ctx.author.name}**")
        else:
            await user.add_roles(role) #adds the role
            await ctx.send(f"Given **{ctx.author.name}** the DXP Pings role")


    dxpSL = ['Server 1', 'Server 2', 'Server 3', 'Server 4', 'Server 5', 'Server 6', 'Server 7', 'Server 8', 'Server 9', 'Server A']

    @bot.command()
    async def online(ctx, vrpid):
        onlineRun = 0
        onlineRun2 = 0
        player = False
        await ctx.send(f"Looking for a player with the ID **{vrpid}**")
        for e in serverL:
            try:
                if debugging == True:
                    await bot.get_channel(879489727177297940).send(f"Looking on {serverL[onlineRun]}")
                onlineS = requests.get(f"{serverN[onlineRun]}status/widget/players.json", timeout=10)
                onlineS = onlineS.json()
                onlineA = onlineS.get('players')
                playerCount = len(onlineA)
                for p in range(playerCount):
                    if debugging == True:
                        await bot.get_channel(879489727177297940).send(f"{onlineA[onlineRun2]}")
                    if int(onlineA[onlineRun2][2]) == int(vrpid):
                        await ctx.channel.purge(limit=1)
                        plyr = onlineA[onlineRun2]
                        em = discord.Embed(title= plyr[0], color=discord.Color.red())

                        em.add_field(name="ID", value=plyr[2], inline=False)
                        em.add_field(name="Server", value=dxpSL[onlineRun], inline=False)
                        em.add_field(name="Job", value=plyr[5], inline=False)
                        em.set_thumbnail(url=plyr[3])

                        await ctx.send(embed = em)
                        player = True
                        break

                    if player == True:
                        break
                    onlineRun2 += 1
            except Exception as e:
                await ctx.send("An exception has occured: {e}")
            onlineRun += 1
        if player == False:
            await ctx.channel.purge(limit=1)
            await ctx.send(f"The player with the id **{vrpid}** is not online right now")


    arg1 = ""
    @bot.command()
    async def test(ctx, arg1=None):
        await ctx.send("<@238771447290527745>")

    debugging = False
    @bot.command()
    async def debug(ctx):
        global debugging
        if ctx.message.author.id == 238771447290527745:
            if debugging == False:
                await ctx.send("Debugging mode active")
                debugging = True
            elif debugging == True:
                await ctx.send("Debugging mode no longer active")
                debugging = False
        else:
            await ctx.send("You do not have access to this command")


    bot.run(token)
else:
    print("a")
