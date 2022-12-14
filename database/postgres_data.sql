--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:utFAbs+L9EahThZMYZ6Z4A==$ESAvKd+hBqIGmWGJ3m4kRkkzhtg1orvR5y4GeB3W/ug=:rnKtmp1k/XPxhOWVG7j3QyvQyAvlYVLcU1QaU8rGsrA=';

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_profile (
    id bigint NOT NULL,
    date_of_birth date,
    user_id integer NOT NULL
);


ALTER TABLE public.account_profile OWNER TO postgres;

--
-- Name: account_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.account_profile ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.account_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: characters_adtcharacter; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.characters_adtcharacter (
    id bigint NOT NULL,
    pid uuid NOT NULL,
    slug character varying(200) NOT NULL,
    name character varying(150) NOT NULL,
    age double precision NOT NULL,
    gender character varying(1) NOT NULL,
    charisma integer NOT NULL,
    constitution integer NOT NULL,
    dexterity integer NOT NULL,
    intelligence integer NOT NULL,
    strength integer NOT NULL,
    wisdom integer NOT NULL,
    level integer NOT NULL,
    experience_points integer NOT NULL,
    character_class character varying(100) NOT NULL,
    race character varying(50) NOT NULL,
    alignment character varying(100) NOT NULL,
    platinum integer NOT NULL,
    gold integer NOT NULL,
    silver integer NOT NULL,
    copper integer NOT NULL,
    image character varying(100) NOT NULL,
    created_by character varying(100) NOT NULL,
    created_date timestamp with time zone NOT NULL,
    category_id bigint NOT NULL,
    CONSTRAINT characters_adtcharacter_experience_points_check CHECK ((experience_points >= 0)),
    CONSTRAINT characters_adtcharacter_level_check CHECK ((level >= 0))
);


ALTER TABLE public.characters_adtcharacter OWNER TO postgres;

--
-- Name: characters_adtcharacter_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.characters_adtcharacter ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.characters_adtcharacter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: characters_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.characters_category (
    id bigint NOT NULL,
    name character varying(200) NOT NULL,
    slug character varying(200) NOT NULL
);


ALTER TABLE public.characters_category OWNER TO postgres;

--
-- Name: characters_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.characters_category ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.characters_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Data for Name: account_profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_profile (id, date_of_birth, user_id) FROM stdin;
1	2022-11-24	2
2	2022-11-24	3
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add profile	7	add_profile
26	Can change profile	7	change_profile
27	Can delete profile	7	delete_profile
28	Can view profile	7	view_profile
29	Can add category	8	add_category
30	Can change category	8	change_category
31	Can delete category	8	delete_category
32	Can view category	8	view_category
33	Can add adt character	9	add_adtcharacter
34	Can change adt character	9	change_adtcharacter
35	Can delete adt character	9	delete_adtcharacter
36	Can view adt character	9	view_adtcharacter
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$390000$2mPKk354FBag49hEge28wR$bTb1PTQLC58e1kiW6Uy1HKWOp4fHpGth2L1ybu/mYe8=	2022-11-25 09:10:15.56777-05	t	adt_admin			adt_admin@email.com	t	t	2022-11-25 08:48:25.81493-05
2	pbkdf2_sha256$390000$8aM8Lxvino5Az31klSsg97$bFxNFAvxlqgJUwusB5+OJoCL6MgZEkYXW7lPXVs0UVU=	2022-11-25 09:15:43.68362-05	f	adt_user1	Dungeon1	User1	adt_user1@email.com	f	t	2022-11-25 08:50:11-05
3	pbkdf2_sha256$390000$01VoNrapUC3a3TFFLqvMZm$TO0wiY4jzJK+9dgOHkR4oMunVtR9U2nT2Hh/ekwAnr4=	2022-11-25 09:36:56.056275-05	f	adt_user2	Dungeon2	User	adt_user2@email.com	f	t	2022-11-25 08:51:02-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: characters_adtcharacter; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.characters_adtcharacter (id, pid, slug, name, age, gender, charisma, constitution, dexterity, intelligence, strength, wisdom, level, experience_points, character_class, race, alignment, platinum, gold, silver, copper, image, created_by, created_date, category_id) FROM stdin;
1	d87d9b3a-8ced-4da7-b635-4587215a1846	cleric	Aenelis Neyphen	266	M	11	15	16	15	13	13	2	12000	cleric	elf	neutral	0	122	12	1222	images/2022/11/25/char8.png	adt_user1	2022-11-25 08:58:05.894121-05	4
2	be0c5c98-6a42-4a95-adf0-f985fdbcde60	fighter	Jeng Nam	18	F	17	14	11	18	18	14	3	12999	fighter	human	neutral	12	3000	112	3334	images/2022/11/25/char2.png	adt_user1	2022-11-25 09:00:17.590935-05	1
\.


--
-- Data for Name: characters_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.characters_category (id, name, slug) FROM stdin;
1	fighter	fighter
2	wizard	wizard
3	barbarian	barbarian
4	cleric	cleric
5	bard	bard
6	druid	druid
7	monk	monk
8	paladin	paladin
9	ranger	ranger
10	rogue	rogue
11	sorcerer	sorcerer
12	warlock	warlock
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-11-25 08:50:11.25792-05	2	adt_user1	1	[{"added": {}}]	4	1
2	2022-11-25 08:50:40.346107-05	2	adt_user1	2	[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]	4	1
3	2022-11-25 08:51:02.346339-05	3	adt_user2	1	[{"added": {}}]	4	1
4	2022-11-25 08:51:25.414511-05	3	adt_user2	2	[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]	4	1
5	2022-11-25 08:51:35.204064-05	1	fighter	1	[{"added": {}}]	8	1
6	2022-11-25 08:51:41.472646-05	2	wizard	1	[{"added": {}}]	8	1
7	2022-11-25 08:52:34.996781-05	3	barbarian	1	[{"added": {}}]	8	1
8	2022-11-25 08:52:49.082694-05	4	cleric	1	[{"added": {}}]	8	1
9	2022-11-25 08:52:55.625066-05	5	bard	1	[{"added": {}}]	8	1
10	2022-11-25 08:53:03.653977-05	6	druid	1	[{"added": {}}]	8	1
11	2022-11-25 08:53:12.165927-05	7	monk	1	[{"added": {}}]	8	1
12	2022-11-25 08:54:03.543533-05	8	paladin	1	[{"added": {}}]	8	1
13	2022-11-25 08:54:08.151705-05	9	ranger	1	[{"added": {}}]	8	1
14	2022-11-25 08:54:21.920351-05	10	rogue	1	[{"added": {}}]	8	1
15	2022-11-25 08:54:27.072174-05	11	sorcerer	1	[{"added": {}}]	8	1
16	2022-11-25 08:54:37.766226-05	12	warlock	1	[{"added": {}}]	8	1
17	2022-11-25 08:58:05.897696-05	1	Name: Aenelis Neyphen, Class: cleric, Race: elf, Level: 2	1	[{"added": {}}]	9	1
18	2022-11-25 09:00:17.591932-05	2	Name: Jeng Nam, Class: fighter, Race: human, Level: 3	1	[{"added": {}}]	9	1
19	2022-11-25 09:07:10.544133-05	1	Profile of adt_user1	1	[{"added": {}}]	7	1
20	2022-11-25 09:07:19.342326-05	2	Profile of adt_user2	1	[{"added": {}}]	7	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	account	profile
8	characters	category
9	characters	adtcharacter
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-11-25 08:46:21.065176-05
2	auth	0001_initial	2022-11-25 08:46:21.214775-05
3	account	0001_initial	2022-11-25 08:46:21.248685-05
4	admin	0001_initial	2022-11-25 08:46:21.285586-05
5	admin	0002_logentry_remove_auto_add	2022-11-25 08:46:21.293565-05
6	admin	0003_logentry_add_action_flag_choices	2022-11-25 08:46:21.302541-05
7	contenttypes	0002_remove_content_type_name	2022-11-25 08:46:21.318497-05
8	auth	0002_alter_permission_name_max_length	2022-11-25 08:46:21.328471-05
9	auth	0003_alter_user_email_max_length	2022-11-25 08:46:21.33645-05
10	auth	0004_alter_user_username_opts	2022-11-25 08:46:21.344432-05
11	auth	0005_alter_user_last_login_null	2022-11-25 08:46:21.357394-05
12	auth	0006_require_contenttypes_0002	2022-11-25 08:46:21.359388-05
13	auth	0007_alter_validators_add_error_messages	2022-11-25 08:46:21.367367-05
14	auth	0008_alter_user_username_max_length	2022-11-25 08:46:21.386319-05
15	auth	0009_alter_user_last_name_max_length	2022-11-25 08:46:21.396871-05
16	auth	0010_alter_group_name_max_length	2022-11-25 08:46:21.407932-05
17	auth	0011_update_proxy_permissions	2022-11-25 08:46:21.415691-05
18	auth	0012_alter_user_first_name_max_length	2022-11-25 08:46:21.425812-05
19	characters	0001_initial	2022-11-25 08:46:21.528652-05
20	sessions	0001_initial	2022-11-25 08:46:21.561479-05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
11ctxho5u320th7ez0o4qxg6f0fnewpv	.eJxVjDkOwjAUBe_iGlk2XmIo6TlD9Bd_HEC2FCcV4u4QKQW0b2beS42wLmVce57HidVZWXX43RDokesG-A711jS1uswT6k3RO-362jg_L7v7d1Cgl2_tgCWejGM-ehLvfHDW2GyEZMCU2DkTs0USIvQgZMgP4CmGmCVZDOr9AfbTOK8:1oyZPD:IGUonWMr2Y0YL0z_LI7KhrFxcBYmLVF6P8tyUlrLi6E	2022-12-09 09:10:15.56877-05
lrsqab5dtvnt1qixo5pqsebter852gls	.eJxVjDsOwjAQRO_iGll2suvdUNLnDJY_GxxAiZRPhbg7jpQCmtFo3sy8lQ_7Vvy-yuLHrK6qVZffLIb0lOkA-RGm-6zTPG3LGPVR0SdddT9ned3O7t9BCWup6yE1ziJ1xmVBlq4xnICBmcR0Qq6BKogWyEW2MQBCNYMFS9gSo_p8AbLyNiI:1oyZp2:WsOJ5Dw8ieUtVoyMZYsv-J-FEjeefbmoflzXtanXuzg	2022-12-09 09:36:56.058274-05
\.


--
-- Name: account_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_profile_id_seq', 2, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 36, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: characters_adtcharacter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.characters_adtcharacter_id_seq', 2, true);


--
-- Name: characters_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.characters_category_id_seq', 12, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 20, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 9, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 20, true);


--
-- Name: account_profile account_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_profile
    ADD CONSTRAINT account_profile_pkey PRIMARY KEY (id);


--
-- Name: account_profile account_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_profile
    ADD CONSTRAINT account_profile_user_id_key UNIQUE (user_id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: characters_adtcharacter characters_adtcharacter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters_adtcharacter
    ADD CONSTRAINT characters_adtcharacter_pkey PRIMARY KEY (id);


--
-- Name: characters_category characters_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters_category
    ADD CONSTRAINT characters_category_pkey PRIMARY KEY (id);


--
-- Name: characters_category characters_category_slug_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters_category
    ADD CONSTRAINT characters_category_slug_key UNIQUE (slug);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: characters_adtcharacter_category_id_f804a248; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_category_id_f804a248 ON public.characters_adtcharacter USING btree (category_id);


--
-- Name: characters_adtcharacter_character_class_b9535241; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_character_class_b9535241 ON public.characters_adtcharacter USING btree (character_class);


--
-- Name: characters_adtcharacter_character_class_b9535241_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_character_class_b9535241_like ON public.characters_adtcharacter USING btree (character_class varchar_pattern_ops);


--
-- Name: characters_adtcharacter_id_slug_01cc7e20_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_id_slug_01cc7e20_idx ON public.characters_adtcharacter USING btree (id, slug);


--
-- Name: characters_adtcharacter_name_92a69ed5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_name_92a69ed5 ON public.characters_adtcharacter USING btree (name);


--
-- Name: characters_adtcharacter_name_92a69ed5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_name_92a69ed5_like ON public.characters_adtcharacter USING btree (name varchar_pattern_ops);


--
-- Name: characters_adtcharacter_slug_68526982; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_slug_68526982 ON public.characters_adtcharacter USING btree (slug);


--
-- Name: characters_adtcharacter_slug_68526982_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_adtcharacter_slug_68526982_like ON public.characters_adtcharacter USING btree (slug varchar_pattern_ops);


--
-- Name: characters_category_name_76a586a5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_category_name_76a586a5 ON public.characters_category USING btree (name);


--
-- Name: characters_category_name_76a586a5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_category_name_76a586a5_like ON public.characters_category USING btree (name varchar_pattern_ops);


--
-- Name: characters_category_slug_9aeea399_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX characters_category_slug_9aeea399_like ON public.characters_category USING btree (slug varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: account_profile account_profile_user_id_bdd52018_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_profile
    ADD CONSTRAINT account_profile_user_id_bdd52018_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: characters_adtcharacter characters_adtcharac_category_id_f804a248_fk_character; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters_adtcharacter
    ADD CONSTRAINT characters_adtcharac_category_id_f804a248_fk_character FOREIGN KEY (category_id) REFERENCES public.characters_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

