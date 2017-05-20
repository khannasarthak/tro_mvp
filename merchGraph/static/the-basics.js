var substringMatcher = function (strs) {
    return function findMatches(q, cb) {
        var matches, substringRegex;

        // an array that will be populated with substring matches
        matches = [];

        // regex used to determine if a string contains the substring `q`
        substrRegex = new RegExp(q, 'i');

        // iterate through the pool of strings and for any string that
        // contains the substring `q`, add it to the `matches` array
        $.each(strs, function (i, str) {
            if (substrRegex.test(str)) {
                matches.push(str);
            }
        });

        cb(matches);
    };
};

var states = ['Amon Ra (moc_pryd06)','Angeling (pay_fild04)','Angeling (xmas_dun01)','Angeling (yuno_fild03)','Archangeling (yuno_fild05)',
'Atroce (ra_fild02)','Atroce (ra_fild03)','Atroce (ra_fild04)','Atroce (ve_fild01)','Atroce (ve_fild02)','Bacsojin (lou_dun03)',
'Baphomet (prt_maze03)','Beelzebub (abbey03)','Boitata (bra_dun02)','Dark Lord (gld_dun04)','Dark Lord (gl_chyard)','Detale (abyss_03)',
'Deviling (pay_fild04)','Deviling (yuno_fild03)','Doppelganger (gef_dun02)','Dracula (gef_dun01)','Drake (treasure02)','Eddga (pay_fild11)',
'Egnigem Cenia (lhz_dun02)','Evil Snake Lord (gon_dun03)','Fallen Bishop Hibram (abbey02)','Garm (xmas_fild01)','Ghostring (pay_fild04)',
'Ghostring (prt_maze03)','Ghostring (treasure02)','Gloom Under Night (ra_san05)','Golden Thief Bug (prt_sewb4)','Gopinich (mosk_dun03)',
'Hardrock Mammoth (man_fild03)','Ifrit (thor_v03)','Incantation Samurai (ama_dun03)','Kiel D-01 (kh_dun02)','Kraken (iz_dun05)',
'Ktullanux (ice_dun03)','Lady Tanee (ayo_dun02)','Leak (dew_dun01)','Lord of Death (niflheim)','Maya (anthell02)','Maya Purple (anthell01)',
'Mistress (mjolnir_04)','Moonlight Flower (pay_dun04)','Orc Hero (gef_fild02)','Orc Hero (gef_fild14)','Orc Lord (gef_fild10)',
'Osiris (moc_pryd04)','Pharaoh (in_sphinx5)','Phreeoni (moc_fild17)','Queen Scaraba (dic_dun02)','RSX-0806 (ein_dun02)','Stormy Knight (xmas_dun02)',
'Tao Gunka (beach_dun)','Tao Gunka (beach_dun2)','Tao Gunka (beach_dun3)','Tendrillion (spl_fild03)','Thanatos (thana_boss)',
'Turtle General (tur_dun04)','Valkyrie Randgris (odin_tem03)','Vesper (jupe_core)','Wounded Morroc (moc_fild22)'
];

$('#the-basics .typeahead').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
}, {
    name: 'states',
    source: substringMatcher(states)
});