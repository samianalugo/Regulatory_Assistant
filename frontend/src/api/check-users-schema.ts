import { Client } from 'pg';

const client = new Client({
  connectionString: 'postgresql://race_management_db_user:ZjMr4YppbEE0shbkM9XLMmOn8QJQQr3g@dpg-d384efgdl3ps73avnjf0-a.frankfurt-postgres.render.com:5432/race_management_db?sslmode=require',
});

async function checkUsersSchema() {
  try {
    await client.connect();
    const res = await client.query(`
      SELECT column_name, data_type
      FROM information_schema.columns
      WHERE table_name = 'users';
    `);
    console.table(res.rows);
  } catch (err) {
    console.error(err);
  } finally {
    await client.end();
  }
}

checkUsersSchema();
