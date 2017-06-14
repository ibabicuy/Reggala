db.plants.aggregate(
    { $match: {
        plant_id : 1
    }},

    { $unwind: '$humidity_data' },

    { $sort: {
        'humidity_data.date': -1
    }},
    {$limit: 1}
)